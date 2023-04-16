from urllib.parse import quote

from typing import Optional
from fusion.models.volume_snapshot_list import VolumeSnapshotList
from fusion.models.volume_snapshot import VolumeSnapshot
from fjuzn.http_client import AsyncHttpClient


class VolumeSnapshotsApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def get_by_id(self, volume_snapshot_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> VolumeSnapshot:
        """
        Gets a specific Volume Snapshot.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_volume_snapshot_by_id_with_http_info(volume_snapshot_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volume_snapshot_id: The Volume Snapshot ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: VolumeSnapshot
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/volume-snapshots/{volume_snapshot_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{volume_snapshot_id}", quote(str(volume_snapshot_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return VolumeSnapshot(**response)

    async def get(self, tenant_name: str, tenant_space_name: str, snapshot_name: str, volume_snapshot_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> VolumeSnapshot:
        """
        Gets a specific Volume Snapshot.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_volume_snapshot_with_http_info(tenant_name, tenant_space_name, snapshot_name, volume_snapshot_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str snapshot_name: The Snapshot name (required)
        :param str volume_snapshot_name: The Volume Snapshot name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: VolumeSnapshot
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/snapshots/{snapshot_name}/volume-snapshots/{volume_snapshot_name}"
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
        url = url.replace("{snapshot_name}", quote(str(snapshot_name), safe=""))
        url = url.replace("{volume_snapshot_name}", quote(str(volume_snapshot_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return VolumeSnapshot(**response)

    async def list(self, tenant_name: str, tenant_space_name: str, snapshot_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, filter: Optional[str] = None, sort: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, id: Optional[str] = None, name: Optional[str] = None, display_name: Optional[str] = None, destroyed: Optional[bool] = None, volume_id: Optional[str] = None, time_remaining: Optional[int] = None, volume_serial_number: Optional[str] = None, placement_group_id: Optional[str] = None, protection_policy_id: Optional[str] = None, created_at: Optional[int] = None, timeout: Optional[float] = None) -> VolumeSnapshotList:
        """
        Gets a list of all Volume snapshots in a Snapshot.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_volume_snapshots_with_http_info(tenant_name, tenant_space_name, snapshot_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str snapshot_name: The Snapshot name (required)
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
        :param bool destroyed:
        :param str volume_id:
        :param int time_remaining:
        :param str volume_serial_number:
        :param str placement_group_id:
        :param str protection_policy_id:
        :param int created_at:
        :return: VolumeSnapshotList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/snapshots/{snapshot_name}/volume-snapshots"
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
        if destroyed is not None:
            query_params.append(("destroyed", destroyed))
        if volume_id is not None:
            query_params.append(("volume_id", volume_id))
        if time_remaining is not None:
            query_params.append(("time_remaining", time_remaining))
        if volume_serial_number is not None:
            query_params.append(("volume_serial_number", volume_serial_number))
        if placement_group_id is not None:
            query_params.append(("placement_group_id", placement_group_id))
        if protection_policy_id is not None:
            query_params.append(("protection_policy_id", protection_policy_id))
        if created_at is not None:
            query_params.append(("created_at", created_at))

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        url = url.replace("{tenant_space_name}", quote(str(tenant_space_name), safe=""))
        url = url.replace("{snapshot_name}", quote(str(snapshot_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return VolumeSnapshotList(**response)
