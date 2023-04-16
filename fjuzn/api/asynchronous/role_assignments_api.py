from fusion.models.role_assignment_post import RoleAssignmentPost
from urllib.parse import quote

from typing import Optional
from fusion.models.role_assignment_ref import RoleAssignmentRef
from typing import List
from fusion.models.role_assignment import RoleAssignment
from fjuzn.http_client import AsyncHttpClient


class RoleAssignmentsApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def create(self, role_assignment: RoleAssignmentPost, role_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> RoleAssignmentRef:
        """
        Creates a Role Assignment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_role_assignment_with_http_info(body, role_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RoleAssignmentPost body: (required)
        :param str role_name: The Role name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/roles/{role_name}/role-assignments"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id
        header_params["Content-Type"] = "application/json"

        query_params = []

        url = url.replace("{role_name}", quote(str(role_name), safe=""))
        response = await self.__client.post(url, query_params, header_params, role_assignment, timeout=timeout)
        
        return RoleAssignmentRef(**response)

    async def delete(self, role_name: str, role_assignment_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> RoleAssignmentRef:
        """
        Delete a Role Assignment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_role_assignment_with_http_info(role_name, role_assignment_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: The Role name (required)
        :param str role_assignment_name: The Role Assignment name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/roles/{role_name}/role-assignments/{role_assignment_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{role_name}", quote(str(role_name), safe=""))
        url = url.replace("{role_assignment_name}", quote(str(role_assignment_name), safe=""))
        response = await self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return RoleAssignmentRef(**response)

    async def get_by_id(self, role_assignment_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> RoleAssignment:
        """
        Gets a specific Role Assignment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_assignment_by_id_with_http_info(role_assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_assignment_id: The Role Assignment ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: RoleAssignment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/role-assignments/{role_assignment_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{role_assignment_id}", quote(str(role_assignment_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return RoleAssignment(**response)

    async def get(self, role_name: str, role_assignment_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> RoleAssignment:
        """
        Gets a specific Role Assignment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_assignment_with_http_info(role_name, role_assignment_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: The Role name (required)
        :param str role_assignment_name: The Role Assignment name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: RoleAssignment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/roles/{role_name}/role-assignments/{role_assignment_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{role_name}", quote(str(role_name), safe=""))
        url = url.replace("{role_assignment_name}", quote(str(role_assignment_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return RoleAssignment(**response)

    async def list_canonical(self, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, scope: Optional[str] = None, principal: Optional[str] = None, role: Optional[str] = None, timeout: Optional[float] = None) -> List[RoleAssignment]:
        """
        Gets a list of all Role Assignments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_assignments_canonical_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :param str scope:
        :param str principal:
        :param str role:
        :return: list[RoleAssignment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/role-assignments"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []
        if scope is not None:
            query_params.append(("scope", scope))
        if principal is not None:
            query_params.append(("principal", principal))
        if role is not None:
            query_params.append(("role", role))

        
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return [RoleAssignment(**r) for r in response]

    async def list(self, role_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, scope: Optional[str] = None, principal: Optional[str] = None, timeout: Optional[float] = None) -> List[RoleAssignment]:
        """
        Gets a list of all Role Assignments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_assignments_with_http_info(role_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: The Role name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :param str scope:
        :param str principal:
        :return: list[RoleAssignment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/roles/{role_name}/role-assignments"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []
        if scope is not None:
            query_params.append(("scope", scope))
        if principal is not None:
            query_params.append(("principal", principal))

        url = url.replace("{role_name}", quote(str(role_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return [RoleAssignment(**r) for r in response]
