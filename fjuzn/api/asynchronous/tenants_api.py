from urllib.parse import quote

from fusion.models.tenant_patch import TenantPatch
from fjuzn.http_client import AsyncHttpClient
from typing import Optional
from fusion.models.tenant_list import TenantList
from fusion.models.tenant_post import TenantPost
from fusion.models.tenant_ref import TenantRef
from fusion.models.space import Space
from fusion.models.tenant import Tenant
from fusion.models.performance import Performance


class TenantsApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def create(self, tenant: TenantPost, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> TenantRef:
        """
        Creates a Tenant.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tenant_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TenantPost body: (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id
        header_params["Content-Type"] = "application/json"

        query_params = []

        
        response = await self.__client.post(url, query_params, header_params, tenant, timeout=timeout)
        
        return TenantRef(**response)

    async def delete(self, tenant_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> None:
        """
        Deletes a specific Tenant.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tenant_with_http_info(tenant_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        response = await self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return None

    async def get_by_id(self, tenant_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Tenant:
        """
        Gets a specific Tenant.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tenant_by_id_with_http_info(tenant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: The Tenant ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/tenants/{tenant_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{tenant_id}", quote(str(tenant_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Tenant(**response)

    async def get_performance(self, tenant_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Performance:
        """
        Gets performance metrics of a specific Tenant.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tenant_performance_with_http_info(tenant_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Performance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/performance"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Performance(**response)

    async def get(self, tenant_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Tenant:
        """
        Gets a specific Tenant.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tenant_with_http_info(tenant_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Tenant(**response)

    async def get_space(self, tenant_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Space:
        """
        Gets space metrics of a specific Tenant.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tenants_space_with_http_info(tenant_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/space"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Space(**response)

    async def list(self, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> TenantList:
        """
        Gets a list of all Tenants.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_tenants_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: TenantList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return TenantList(**response)

    async def update(self, tenant: TenantPatch, tenant_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> TenantRef:
        """
        Updates a Tenant.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_tenant_with_http_info(body, tenant_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TenantPatch body: (required)
        :param str tenant_name: The Tenant name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}"
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
        response = await self.__client.patch(url, query_params, header_params, tenant, timeout=timeout)
        
        return TenantRef(**response)
