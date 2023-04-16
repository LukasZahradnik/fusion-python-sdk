import inspect
import importlib
import re

from pathlib import Path

camel_to_snake_pattern = re.compile("(.)([A-Z][a-z]+)")
camel_to_snake_pattern_0 = re.compile("([a-z0-9])([A-Z])")

doc_to_type = re.compile(":param ([a-zA-Z_]*) ([a-zA-Z_]*):")
header_re = re.compile("header_params\['(.*)'] = params\['(.*)']")
param_re = re.compile("query_params.append\(\('(.*)', params\['(.*)']\)\)")
path_param_re = re.compile("path_params\['(.*)'] = params\['(.*)']")

return_type_re = re.compile(":return: (.*)")
return_url_method = re.compile(r"return self.api_client.call_api\(\s*\'(.*)\',\s*\'(.*)\'")


def camel_to_snake(name):
    name = camel_to_snake_pattern.sub(r"\1_\2", name)
    return camel_to_snake_pattern_0.sub(r"\1_\2", name).lower()


output_path = Path("fjuzn/api/synchronous")
input_path = Path("./fusion/api")

async_code = False


class_template = """
class {class_name}:
    __slots__ = "__client",
    
    def __init__(self, client: {http_client_type}):
        self.__client = client
"""

method_template = '''
    {func_def} {method_name}({method_args}) -> {method_return_type}:
        """
        {docs}
        """
        url = "{url_path}"
        {header_params}
        {query_params}
        {path_params}
        response = {response_get}self.__client.{method}(url, query_params, header_params{body}, timeout=timeout)
        
        return {return_type}
'''

for file in input_path.iterdir():
    module_name_parts = str(file).split("/")
    if module_name_parts[-1].startswith("_"):  # Skip __pycache__ etc.
        continue

    module_name = ".".join(module_name_parts)[:-3]
    module = importlib.import_module(module_name)

    imports = {
        "from typing import Optional",
        "from urllib.parse import quote\n",
        "from fjuzn.http_client import AsyncHttpClient" if async_code else "from fjuzn.http_client import HttpClient",
    }

    source_code = []

    for class_name, class_obj in inspect.getmembers(module, inspect.isclass):
        if class_name == "ApiClient":  # Ignore re-exporting ApiClient
            continue

        plural_resource_name = camel_to_snake(class_name).replace("_api", "")
        if plural_resource_name.endswith("ses"):
            singular_resource_name = plural_resource_name[:-2]
        else:
            singular_resource_name = plural_resource_name[:-1]  # plural to singular
        if singular_resource_name.endswith("ie"):  # policies -> policy
            singular_resource_name = f"{singular_resource_name[:-2]}y"

        client_type = "AsyncHttpClient" if async_code else "HttpClient"
        source_code.append(class_template.format(class_name=class_name, http_client_type=client_type))

        for method_name, method_obj in inspect.getmembers(class_obj(), predicate=inspect.ismethod):
            if method_name == "__init__" or not method_name.endswith("_http_info"):  # Don't care
                continue

            method_info = inspect.getfullargspec(method_obj)
            method_args = [arg if arg != "body" else singular_resource_name for arg in method_info.args]

            new_method_name = method_name[:-15].replace(plural_resource_name, "")
            new_method_name = new_method_name.replace(singular_resource_name, "").replace("__", "_")

            if new_method_name.endswith("_"):
                new_method_name = new_method_name[:-1]

            arg_types = {match.group(2): match.group(1) for match in doc_to_type.finditer(method_obj.__doc__)}
            if "body" in arg_types:
                arg_types[singular_resource_name] = arg_types["body"]
                del arg_types["body"]

            args_set = set(method_args)

            typed_args = ["self"] if "self" in args_set else []
            typed_args.extend([f"{arg}: {arg_types[arg]}" for arg in method_args if arg != "self"])

            typed_kwargs = [f"timeout: Optional[float] = None"]
            if method_info.varkw:
                typed_kwargs = [f"{arg}: Optional[{type}] = None" for arg, type in arg_types.items() if arg not in args_set] + typed_kwargs

            arg_string = ""
            if typed_args:
                arg_string = ", ".join(typed_args)
            if typed_kwargs:
                if typed_args:
                    arg_string = f"{arg_string}, *, {', '.join(typed_kwargs)}"
                else:
                    arg_string = f"*, {', '.join(typed_kwargs)}"

            url_path = ""
            method = ""

            path_params = []
            query_params = [f'query_params = []\n']
            return_type = "None"
            header_params = [f'header_params = {{"Accept": "application/json"}}\n']

            method_source = inspect.getsource(method_obj)

            match = return_url_method.search(method_source)
            if match:
                url_path = match.group(1)
                method = match.group(2)

            match = return_type_re.search(method_source)
            if match:
                return_type = match.group(1)

            for match in path_param_re.finditer(method_source):
                replace_match = "{" + match.group(1) + "}"

                path_params.append(f'{" " * 8}url = url.replace("{replace_match}", quote(str({match.group(2)}), safe=""))\n')

            for match in header_re.finditer(method_source):
                header_params.append(
                    f"{' ' * 8}if {match.group(2)} is not None:\n{' ' * 12}header_params[\"{match.group(1)}\"] = {match.group(2)}\n"
                )

            for match in param_re.finditer(method_source):
                query_params.append(
                    f"{' ' * 8}if {match.group(2)} is not None:\n{' ' * 12}query_params.append((\"{match.group(1)}\", {match.group(2)}))\n"
                )

            if "header_params['Content-Type'] =" in method_source:
                header_params.append(f'{" " * 8}header_params["Content-Type"] = "application/json"\n')

            if return_type == "Operation":
                old_return_type = return_type
                try:
                    return_type = "".join(n.title() for n in singular_resource_name.split("_")) + "Ref"
                    importlib.import_module(old_return_type)
                except:
                    return_type = old_return_type

            is_list = False
            if return_type.startswith("list["):
                return_type = return_type[5:-1]
                imports.add("from typing import List")
                is_list = True
            if return_type is not None:
                imports.add(f"from fusion.models.{camel_to_snake(return_type)} import {return_type}")
            if singular_resource_name in arg_types:
                body_type = arg_types[singular_resource_name]
                imports.add(f"from fusion.models.{camel_to_snake(body_type)} import {body_type}")

            source_code.append(
                method_template.format(
                    func_def="async def" if async_code else "def",
                    method_name=new_method_name,
                    method_args=arg_string,
                    method_return_type=return_type if not is_list else f"List[{return_type}]",
                    docs=method_obj.__doc__.strip(),
                    url_path=url_path,
                    header_params="".join(header_params),
                    query_params="".join(query_params),
                    path_params="".join(path_params).strip(),
                    response_get="await " if async_code else "",
                    method=method.lower(),
                    body=f", {singular_resource_name}" if singular_resource_name in arg_types else "",
                    return_type=f"{return_type}(**response)" if not is_list else f"[{return_type}(**r) for r in response]",
                )
            )

    with open(output_path / module_name_parts[-1], mode="w") as file:
        file.write("\n".join(imports))
        file.write("\n\n")
        file.write("".join(source_code))


from fjuzn import FusionClient, AsyncFusionClient