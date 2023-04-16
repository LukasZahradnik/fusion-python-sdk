from typing import List
from fusion.models.role import Role
from fjuzn.http_client import HttpClient
from typing import Optional
from urllib.parse import quote



class RolesApi:
    __slots__ = "__client",
    
    def __init__(self, client: HttpClient):
        self.__client = client

    def get_by_id(self, role_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Role:
        """
        Gets a specific Role.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_by_id_with_http_info(role_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_id: The Role ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/roles/{role_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{role_id}", quote(str(role_id), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Role(**response)

    def get(self, role_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Role:
        """
        Gets a specific Role.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_with_http_info(role_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: The Role name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/roles/{role_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{role_name}", quote(str(role_name), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Role(**response)

    def list(self, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, assignable_scope: Optional[str] = None, timeout: Optional[float] = None) -> List[Role]:
        """
        Gets a list of all Roles.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_roles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :param str assignable_scope:
        :return: list[Role]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/roles"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []
        if assignable_scope is not None:
            query_params.append(("assignable_scope", assignable_scope))

        
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return [Role(**r) for r in response]
