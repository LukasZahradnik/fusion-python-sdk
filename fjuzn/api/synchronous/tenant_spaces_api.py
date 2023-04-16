from fusion.models.performance import Performance
from fusion.models.tenant_space_list import TenantSpaceList
from fusion.models.operation import Operation
from fjuzn.http_client import HttpClient
from fusion.models.tenant_space_patch import TenantSpacePatch
from fusion.models.tenant_space import TenantSpace
from typing import Optional
from urllib.parse import quote

from fusion.models.space import Space
from fusion.models.tenant_space_post import TenantSpacePost


class TenantSpacesApi:
    __slots__ = "__client",
    
    def __init__(self, client: HttpClient):
        self.__client = client

    def create(self, tenant_space: TenantSpacePost, tenant_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Creates a Tenant Space.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tenant_space_with_http_info(body, tenant_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TenantSpacePost body: (required)
        :param str tenant_name: The Tenant name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id
        header_params["Content-Type"] = "application/json"

        query_params = []

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        response = self.__client.post(url, query_params, header_params, tenant_space, timeout=timeout)
        
        return Operation(**response)

    def delete(self, tenant_name: str, tenant_space_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Deletes a specific Tenant Space.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tenant_space_with_http_info(tenant_name, tenant_space_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        url = url.replace("{tenant_space_name}", quote(str(tenant_space_name), safe=""))
        response = self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return Operation(**response)

    def get_by_id(self, tenant_space_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> TenantSpace:
        """
        Gets a specific Tenant Space.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tenant_space_by_id_with_http_info(tenant_space_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_space_id: The Tenant Space ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: TenantSpace
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/tenant-spaces/{tenant_space_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{tenant_space_id}", quote(str(tenant_space_id), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return TenantSpace(**response)

    def get_performance(self, tenant_name: str, tenant_space_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Performance:
        """
        Gets performance metrics of a specific Tenant Space.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tenant_space_performance_with_http_info(tenant_name, tenant_space_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Performance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/performance"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        url = url.replace("{tenant_space_name}", quote(str(tenant_space_name), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Performance(**response)

    def get_space(self, tenant_name: str, tenant_space_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Space:
        """
        Gets space metrics of a specific Tenant Space.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tenant_space_space_with_http_info(tenant_name, tenant_space_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/space"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        url = url.replace("{tenant_space_name}", quote(str(tenant_space_name), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Space(**response)

    def get(self, tenant_name: str, tenant_space_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> TenantSpace:
        """
        Gets a specific Tenant Space.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tenant_space_with_http_info(tenant_name, tenant_space_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: TenantSpace
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        url = url.replace("{tenant_space_name}", quote(str(tenant_space_name), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return TenantSpace(**response)

    def list(self, tenant_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, filter: Optional[str] = None, sort: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, id: Optional[str] = None, name: Optional[str] = None, display_name: Optional[str] = None, timeout: Optional[float] = None) -> TenantSpaceList:
        """
        Gets a list of all Tenant Spaces.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_tenant_spaces_with_http_info(tenant_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :param str filter: filter should use expression language for filtering
        :param str sort: Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. "sort=size-,name")
        :param int limit:
        :param int offset:
        :param str id:
        :param str name:
        :param str display_name:
        :return: TenantSpaceList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []
        if filter is not None:
            query_params.append(("filter", filter))
        if sort is not None:
            query_params.append(("sort", sort))
        if limit is not None:
            query_params.append(("limit", limit))
        if offset is not None:
            query_params.append(("offset", offset))
        if id is not None:
            query_params.append(("id", id))
        if name is not None:
            query_params.append(("name", name))
        if display_name is not None:
            query_params.append(("display_name", display_name))

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return TenantSpaceList(**response)

    def query(self, *, filter: Optional[str] = None, sort: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, id: Optional[str] = None, name: Optional[str] = None, display_name: Optional[str] = None, tenant_id: Optional[str] = None, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> TenantSpaceList:
        """
        (Opt-in) Get all Tenant Spaces in the org. Provide a filter to search for specific Tenant Spaces  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_tenant_spaces_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter: filter should use expression language for filtering
        :param str sort: Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. "sort=size-,name")
        :param int limit:
        :param int offset:
        :param str id:
        :param str name:
        :param str display_name:
        :param str tenant_id:
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: TenantSpaceList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/tenant-spaces"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []
        if filter is not None:
            query_params.append(("filter", filter))
        if sort is not None:
            query_params.append(("sort", sort))
        if limit is not None:
            query_params.append(("limit", limit))
        if offset is not None:
            query_params.append(("offset", offset))
        if id is not None:
            query_params.append(("id", id))
        if name is not None:
            query_params.append(("name", name))
        if display_name is not None:
            query_params.append(("display_name", display_name))
        if tenant_id is not None:
            query_params.append(("tenant_id", tenant_id))

        
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return TenantSpaceList(**response)

    def update(self, tenant_space: TenantSpacePatch, tenant_name: str, tenant_space_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Updates a Tenant Space.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_tenant_space_with_http_info(body, tenant_name, tenant_space_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TenantSpacePatch body: (required)
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id
        header_params["Content-Type"] = "application/json"

        query_params = []

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        url = url.replace("{tenant_space_name}", quote(str(tenant_space_name), safe=""))
        response = self.__client.patch(url, query_params, header_params, tenant_space, timeout=timeout)
        
        return Operation(**response)
