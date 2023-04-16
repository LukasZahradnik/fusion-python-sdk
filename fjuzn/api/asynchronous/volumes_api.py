from fusion.models.volume import Volume
from fusion.models.volume_list import VolumeList
from urllib.parse import quote

from typing import Optional
from fusion.models.volum_ref import VolumRef
from fusion.models.space import Space
from fusion.models.performance import Performance
from fusion.models.volume_patch import VolumePatch
from fusion.models.volume_post import VolumePost
from fjuzn.http_client import AsyncHttpClient


class VolumesApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def create_e(self, volum: VolumePost, tenant_name: str, tenant_space_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> VolumRef:
        """
        Creates a Volume.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_volume_with_http_info(body, tenant_name, tenant_space_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VolumePost body: (required)
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes"
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
        response = await self.__client.post(url, query_params, header_params, volum, timeout=timeout)
        
        return VolumRef(**response)

    async def delete_e(self, tenant_name: str, tenant_space_name: str, volume_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> VolumRef:
        """
        Eradicate a specific volume. Volume has to be destroyed before it can be eradicated.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_volume_with_http_info(tenant_name, tenant_space_name, volume_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str volume_name: The Volume name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name}"
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
        url = url.replace("{volume_name}", quote(str(volume_name), safe=""))
        response = await self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return VolumRef(**response)

    async def get_e_by_id(self, volume_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Volume:
        """
        Gets a specific Volume.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_volume_by_id_with_http_info(volume_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volume_id: The Volume ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Volume
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/volumes/{volume_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{volume_id}", quote(str(volume_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Volume(**response)

    async def get_e_performance(self, tenant_name: str, tenant_space_name: str, volume_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Performance:
        """
        (Provider) Gets performance metrics of a specific Volume.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_volume_performance_with_http_info(tenant_name, tenant_space_name, volume_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str volume_name: The Volume name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Performance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name}/performance"
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
        url = url.replace("{volume_name}", quote(str(volume_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Performance(**response)

    async def get_e_space(self, tenant_name: str, tenant_space_name: str, volume_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Space:
        """
        (Provider) Gets space metrics of a specific Volume.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_volume_space_with_http_info(tenant_name, tenant_space_name, volume_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str volume_name: The Volume name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name}/space"
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
        url = url.replace("{volume_name}", quote(str(volume_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Space(**response)

    async def get_e(self, tenant_name: str, tenant_space_name: str, volume_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Volume:
        """
        Gets a specific Volume.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_volume_with_http_info(tenant_name, tenant_space_name, volume_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str volume_name: The Volume name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Volume
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name}"
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
        url = url.replace("{volume_name}", quote(str(volume_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Volume(**response)

    async def list(self, tenant_name: str, tenant_space_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, filter: Optional[str] = None, sort: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, id: Optional[str] = None, name: Optional[str] = None, display_name: Optional[str] = None, serial_number: Optional[str] = None, size: Optional[int] = None, created_at: Optional[int] = None, storage_class_id: Optional[str] = None, placement_group_id: Optional[str] = None, protection_policy_id: Optional[str] = None, array_id: Optional[str] = None, source_volume_snapshot_id: Optional[str] = None, iqn: Optional[str] = None, destroyed: Optional[bool] = None, time_remaining: Optional[int] = None, timeout: Optional[float] = None) -> VolumeList:
        """
        Gets a list of all Volumes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_volumes_with_http_info(tenant_name, tenant_space_name, async_req=True)
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
        :param str serial_number:
        :param int size:
        :param int created_at:
        :param str storage_class_id:
        :param str placement_group_id:
        :param str protection_policy_id:
        :param str array_id:
        :param str source_volume_snapshot_id:
        :param str iqn:
        :param bool destroyed:
        :param int time_remaining:
        :return: VolumeList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes"
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
        if serial_number is not None:
            query_params.append(("serial_number", serial_number))
        if size is not None:
            query_params.append(("size", size))
        if created_at is not None:
            query_params.append(("created_at", created_at))
        if storage_class_id is not None:
            query_params.append(("storage_class_id", storage_class_id))
        if placement_group_id is not None:
            query_params.append(("placement_group_id", placement_group_id))
        if protection_policy_id is not None:
            query_params.append(("protection_policy_id", protection_policy_id))
        if array_id is not None:
            query_params.append(("array_id", array_id))
        if source_volume_snapshot_id is not None:
            query_params.append(("source_volume_snapshot_id", source_volume_snapshot_id))
        if iqn is not None:
            query_params.append(("iqn", iqn))
        if destroyed is not None:
            query_params.append(("destroyed", destroyed))
        if time_remaining is not None:
            query_params.append(("time_remaining", time_remaining))

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        url = url.replace("{tenant_space_name}", quote(str(tenant_space_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return VolumeList(**response)

    async def query(self, *, filter: Optional[str] = None, sort: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, id: Optional[str] = None, name: Optional[str] = None, display_name: Optional[str] = None, serial_number: Optional[str] = None, size: Optional[int] = None, created_at: Optional[int] = None, tenant_space_id: Optional[str] = None, tenant_id: Optional[str] = None, storage_class_id: Optional[str] = None, placement_group_id: Optional[str] = None, protection_policy_id: Optional[str] = None, array_id: Optional[str] = None, source_volume_snapshot_id: Optional[str] = None, iqn: Optional[str] = None, destroyed: Optional[bool] = None, time_remaining: Optional[int] = None, host_access_policy_id: Optional[str] = None, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> VolumeList:
        """
        (Opt-in) Get all Volumes in the org. Provide a filter to search for specific volumes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_volumes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter: filter should use expression language for filtering
        :param str sort: Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. "sort=size-,name")
        :param int limit:
        :param int offset:
        :param str id:
        :param str name:
        :param str display_name:
        :param str serial_number:
        :param int size:
        :param int created_at:
        :param str tenant_space_id:
        :param str tenant_id:
        :param str storage_class_id:
        :param str placement_group_id:
        :param str protection_policy_id:
        :param str array_id:
        :param str source_volume_snapshot_id:
        :param str iqn:
        :param bool destroyed:
        :param int time_remaining:
        :param str host_access_policy_id:
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: VolumeList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/volumes"
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
        if serial_number is not None:
            query_params.append(("serial_number", serial_number))
        if size is not None:
            query_params.append(("size", size))
        if created_at is not None:
            query_params.append(("created_at", created_at))
        if tenant_space_id is not None:
            query_params.append(("tenant_space_id", tenant_space_id))
        if tenant_id is not None:
            query_params.append(("tenant_id", tenant_id))
        if storage_class_id is not None:
            query_params.append(("storage_class_id", storage_class_id))
        if placement_group_id is not None:
            query_params.append(("placement_group_id", placement_group_id))
        if protection_policy_id is not None:
            query_params.append(("protection_policy_id", protection_policy_id))
        if array_id is not None:
            query_params.append(("array_id", array_id))
        if source_volume_snapshot_id is not None:
            query_params.append(("source_volume_snapshot_id", source_volume_snapshot_id))
        if iqn is not None:
            query_params.append(("iqn", iqn))
        if destroyed is not None:
            query_params.append(("destroyed", destroyed))
        if time_remaining is not None:
            query_params.append(("time_remaining", time_remaining))
        if host_access_policy_id is not None:
            query_params.append(("host_access_policy_id", host_access_policy_id))

        
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return VolumeList(**response)

    async def update_e(self, volum: VolumePatch, tenant_name: str, tenant_space_name: str, volume_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> VolumRef:
        """
        Updates a Volume -- renaming, and resizing it; changing its Storage Class; changing its Placement Group; adding or removing host connections.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_volume_with_http_info(body, tenant_name, tenant_space_name, volume_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VolumePatch body: (required)
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str volume_name: The Volume name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name}"
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
        url = url.replace("{volume_name}", quote(str(volume_name), safe=""))
        response = await self.__client.patch(url, query_params, header_params, volum, timeout=timeout)
        
        return VolumRef(**response)
