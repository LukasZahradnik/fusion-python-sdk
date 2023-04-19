from fusion.models.placement_group_post import PlacementGroupPost
from urllib.parse import quote

from fusion.models.placement_group_list import PlacementGroupList
from fjuzn.http_client import AsyncHttpClient
from typing import Optional
from fusion.models.placement_group_patch import PlacementGroupPatch
from fusion.models.placement_group_ref import PlacementGroupRef
from fusion.models.space import Space
from fusion.models.placement_group import PlacementGroup
from fusion.models.session_list import SessionList
from fusion.models.performance import Performance


class PlacementGroupsApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def create(self, placement_group: PlacementGroupPost, tenant_name: str, tenant_space_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> PlacementGroupRef:
        """
        Creates a Placement Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_placement_group_with_http_info(body, tenant_name, tenant_space_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PlacementGroupPost body: (required)
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups"
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
        response = await self.__client.post(url, query_params, header_params, placement_group, timeout=timeout)
        
        return PlacementGroupRef(**response)

    async def delete(self, tenant_name: str, tenant_space_name: str, placement_group_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> None:
        """
        Deletes a specific Placement Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_placement_group_with_http_info(tenant_name, tenant_space_name, placement_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str placement_group_name: The Placement Group name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups/{placement_group_name}"
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
        url = url.replace("{placement_group_name}", quote(str(placement_group_name), safe=""))
        response = await self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return None

    async def get_by_id(self, placement_group_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> PlacementGroup:
        """
        Gets a specific Placement Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_placement_group_by_id_with_http_info(placement_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str placement_group_id: The Placement Group ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: PlacementGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/placement-groups/{placement_group_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{placement_group_id}", quote(str(placement_group_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return PlacementGroup(**response)

    async def get_sessions(self, tenant_name: str, tenant_space_name: str, placement_group_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> SessionList:
        """
        Gets iSCSI sessions data of a specific Placement Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_placement_group_sessions_with_http_info(tenant_name, tenant_space_name, placement_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str placement_group_name: The Placement Group name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: SessionList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups/{placement_group_name}/sessions"
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
        url = url.replace("{placement_group_name}", quote(str(placement_group_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return SessionList(**response)

    async def get(self, tenant_name: str, tenant_space_name: str, placement_group_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> PlacementGroup:
        """
        Gets a specific Placement Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_placement_group_with_http_info(tenant_name, tenant_space_name, placement_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str placement_group_name: The Placement Group name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: PlacementGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups/{placement_group_name}"
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
        url = url.replace("{placement_group_name}", quote(str(placement_group_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return PlacementGroup(**response)

    async def get_performance(self, tenant_name: str, tenant_space_name: str, placement_group_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Performance:
        """
        Get performance metrics of a specific Placement Group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_placement_groups_performance_with_http_info(tenant_name, tenant_space_name, placement_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str placement_group_name: The Placement Group name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Performance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups/{placement_group_name}/performance"
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
        url = url.replace("{placement_group_name}", quote(str(placement_group_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Performance(**response)

    async def get_space(self, tenant_name: str, tenant_space_name: str, placement_group_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Space:
        """
        Get space metrics of a specific Placement Group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_placement_groups_space_with_http_info(tenant_name, tenant_space_name, placement_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str placement_group_name: The Placement Group name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups/{placement_group_name}/space"
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
        url = url.replace("{placement_group_name}", quote(str(placement_group_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Space(**response)

    async def list(self, tenant_name: str, tenant_space_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, filter: Optional[str] = None, sort: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, id: Optional[str] = None, name: Optional[str] = None, display_name: Optional[str] = None, array_id: Optional[str] = None, iqn: Optional[str] = None, storage_service_id: Optional[str] = None, availability_zone_id: Optional[str] = None, placement_engine: Optional[str] = None, timeout: Optional[float] = None) -> PlacementGroupList:
        """
        Gets a list of all Placement Groups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_placement_groups_with_http_info(tenant_name, tenant_space_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
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
        :param str array_id:
        :param str iqn:
        :param str storage_service_id:
        :param str availability_zone_id:
        :param str placement_engine:
        :return: PlacementGroupList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups"
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
        if array_id is not None:
            query_params.append(("array_id", array_id))
        if iqn is not None:
            query_params.append(("iqn", iqn))
        if storage_service_id is not None:
            query_params.append(("storage_service_id", storage_service_id))
        if availability_zone_id is not None:
            query_params.append(("availability_zone_id", availability_zone_id))
        if placement_engine is not None:
            query_params.append(("placement_engine", placement_engine))

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        url = url.replace("{tenant_space_name}", quote(str(tenant_space_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return PlacementGroupList(**response)

    async def query(self, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, filter: Optional[str] = None, sort: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, id: Optional[str] = None, name: Optional[str] = None, display_name: Optional[str] = None, tenant_space_id: Optional[str] = None, tenant_id: Optional[str] = None, array_id: Optional[str] = None, iqn: Optional[str] = None, storage_service_id: Optional[str] = None, availability_zone_id: Optional[str] = None, placement_engine: Optional[str] = None, region_name: Optional[str] = None, availability_zone_name: Optional[str] = None, array_name: Optional[str] = None, timeout: Optional[float] = None) -> PlacementGroupList:
        """
        Returns a list of Placement Groups from query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_placement_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
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
        :param str tenant_space_id:
        :param str tenant_id:
        :param str array_id:
        :param str iqn:
        :param str storage_service_id:
        :param str availability_zone_id:
        :param str placement_engine:
        :param str region_name: Region that array belongs to.
        :param str availability_zone_name: Availability zone that array belongs to.
        :param str array_name: Return placement-groups across all tenant spaces that are located on the array. (region_name and availability_zone_name required)
        :return: PlacementGroupList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/placement-groups"
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
        if tenant_space_id is not None:
            query_params.append(("tenant_space_id", tenant_space_id))
        if tenant_id is not None:
            query_params.append(("tenant_id", tenant_id))
        if array_id is not None:
            query_params.append(("array_id", array_id))
        if iqn is not None:
            query_params.append(("iqn", iqn))
        if storage_service_id is not None:
            query_params.append(("storage_service_id", storage_service_id))
        if availability_zone_id is not None:
            query_params.append(("availability_zone_id", availability_zone_id))
        if placement_engine is not None:
            query_params.append(("placement_engine", placement_engine))
        if region_name is not None:
            query_params.append(("region_name", region_name))
        if availability_zone_name is not None:
            query_params.append(("availability_zone_name", availability_zone_name))
        if array_name is not None:
            query_params.append(("array_name", array_name))

        
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return PlacementGroupList(**response)

    async def update(self, placement_group: PlacementGroupPatch, tenant_name: str, tenant_space_name: str, placement_group_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> PlacementGroupRef:
        """
        Updates a specific Placement Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_placement_group_with_http_info(body, tenant_name, tenant_space_name, placement_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PlacementGroupPatch body: (required)
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str placement_group_name: The Placement Group name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups/{placement_group_name}"
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
        url = url.replace("{placement_group_name}", quote(str(placement_group_name), safe=""))
        response = await self.__client.patch(url, query_params, header_params, placement_group, timeout=timeout)
        
        return PlacementGroupRef(**response)
