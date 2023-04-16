from fusion.models.snapshot_patch import SnapshotPatch
from fusion.models.snapshot import Snapshot
from typing import Optional
from fusion.models.snapshot_list import SnapshotList
from fusion.models.operation import Operation
from fjuzn.http_client import AsyncHttpClient
from urllib.parse import quote

from fusion.models.snapshot_post import SnapshotPost


class SnapshotsApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def create(self, snapshot: SnapshotPost, tenant_name: str, tenant_space_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Creates Volume snapshots of specified Volume names.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_snapshot_with_http_info(body, tenant_name, tenant_space_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SnapshotPost body: (required)
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/snapshots"
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
        response = await self.__client.post(url, query_params, header_params, snapshot, timeout=timeout)
        
        return Operation(**response)

    async def delete(self, tenant_name: str, tenant_space_name: str, snapshot_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Eradicate a snapshot and its volume snapshots which were previously marked for deletion using PATCH.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_snapshot_with_http_info(tenant_name, tenant_space_name, snapshot_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str snapshot_name: The Snapshot name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/snapshots/{snapshot_name}"
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
        response = await self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return Operation(**response)

    async def get_by_id(self, snapshot_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Snapshot:
        """
        Gets a specific Snapshot.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_snapshot_by_id_with_http_info(snapshot_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str snapshot_id: The Snapshot ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Snapshot
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/snapshots/{snapshot_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{snapshot_id}", quote(str(snapshot_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Snapshot(**response)

    async def get(self, tenant_name: str, tenant_space_name: str, snapshot_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Snapshot:
        """
        Gets a specific Snapshot.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_snapshot_with_http_info(tenant_name, tenant_space_name, snapshot_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str snapshot_name: The Snapshot name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Snapshot
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/snapshots/{snapshot_name}"
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
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Snapshot(**response)

    async def list(self, tenant_name: str, tenant_space_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, filter: Optional[str] = None, sort: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, id: Optional[str] = None, name: Optional[str] = None, display_name: Optional[str] = None, protection_policy_id: Optional[str] = None, destroyed: Optional[bool] = None, time_remaining: Optional[int] = None, volume: Optional[str] = None, placement_group: Optional[str] = None, timeout: Optional[float] = None) -> SnapshotList:
        """
        Gets a list of Snapshots.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_snapshots_with_http_info(tenant_name, tenant_space_name, async_req=True)
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
        :param str protection_policy_id:
        :param bool destroyed:
        :param int time_remaining:
        :param str volume: Returns only snapshots which contain the given volume
        :param str placement_group: Returns only snapshots in the specified placement group. Cannot be specified together with volume
        :return: SnapshotList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/snapshots"
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
        if protection_policy_id is not None:
            query_params.append(("protection_policy_id", protection_policy_id))
        if destroyed is not None:
            query_params.append(("destroyed", destroyed))
        if time_remaining is not None:
            query_params.append(("time_remaining", time_remaining))
        if volume is not None:
            query_params.append(("volume", volume))
        if placement_group is not None:
            query_params.append(("placement_group", placement_group))

        url = url.replace("{tenant_name}", quote(str(tenant_name), safe=""))
        url = url.replace("{tenant_space_name}", quote(str(tenant_space_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return SnapshotList(**response)

    async def query(self, *, filter: Optional[str] = None, sort: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, id: Optional[str] = None, name: Optional[str] = None, display_name: Optional[str] = None, tenant_space_id: Optional[str] = None, tenant_id: Optional[str] = None, protection_policy_id: Optional[str] = None, destroyed: Optional[bool] = None, time_remaining: Optional[int] = None, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> SnapshotList:
        """
        (Opt-in) Get all Snapshots in the org. Provide a filter to search for specific snapshots.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_snapshots_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter: filter should use expression language for filtering
        :param str sort: Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. "sort=size-,name")
        :param int limit:
        :param int offset:
        :param str id:
        :param str name:
        :param str display_name:
        :param str tenant_space_id:
        :param str tenant_id:
        :param str protection_policy_id:
        :param bool destroyed:
        :param int time_remaining:
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: SnapshotList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/snapshots"
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
        if protection_policy_id is not None:
            query_params.append(("protection_policy_id", protection_policy_id))
        if destroyed is not None:
            query_params.append(("destroyed", destroyed))
        if time_remaining is not None:
            query_params.append(("time_remaining", time_remaining))

        
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return SnapshotList(**response)

    async def update(self, snapshot: SnapshotPatch, tenant_name: str, tenant_space_name: str, snapshot_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Recovers a pending snapshot  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_snapshot_with_http_info(body, tenant_name, tenant_space_name, snapshot_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SnapshotPatch body: (required)
        :param str tenant_name: The Tenant name (required)
        :param str tenant_space_name: The Tenant Space name (required)
        :param str snapshot_name: The Snapshot name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/snapshots/{snapshot_name}"
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
        url = url.replace("{snapshot_name}", quote(str(snapshot_name), safe=""))
        response = await self.__client.patch(url, query_params, header_params, snapshot, timeout=timeout)
        
        return Operation(**response)
