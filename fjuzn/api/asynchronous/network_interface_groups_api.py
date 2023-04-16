from fusion.models.network_interface_group_post import NetworkInterfaceGroupPost
from fusion.models.network_interface_group_patch import NetworkInterfaceGroupPatch
from typing import Optional
from fusion.models.operation import Operation
from fjuzn.http_client import AsyncHttpClient
from urllib.parse import quote

from fusion.models.network_interface_group import NetworkInterfaceGroup
from fusion.models.network_interface_group_list import NetworkInterfaceGroupList


class NetworkInterfaceGroupsApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def create(self, network_interface_group: NetworkInterfaceGroupPost, region_name: str, availability_zone_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        (Provider) Creates a Network Interface Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_network_interface_group_with_http_info(body, region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NetworkInterfaceGroupPost body: (required)
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/network-interface-groups"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id
        header_params["Content-Type"] = "application/json"

        query_params = []

        url = url.replace("{region_name}", quote(str(region_name), safe=""))
        url = url.replace("{availability_zone_name}", quote(str(availability_zone_name), safe=""))
        response = await self.__client.post(url, query_params, header_params, network_interface_group, timeout=timeout)
        
        return Operation(**response)

    async def delete(self, region_name: str, availability_zone_name: str, network_interface_group_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        (Provider) Deletes a specific Network Interface Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_network_interface_group_with_http_info(region_name, availability_zone_name, network_interface_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str network_interface_group_name: (Provider) The Network Interface Group name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/network-interface-groups/{network_interface_group_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{region_name}", quote(str(region_name), safe=""))
        url = url.replace("{availability_zone_name}", quote(str(availability_zone_name), safe=""))
        url = url.replace("{network_interface_group_name}", quote(str(network_interface_group_name), safe=""))
        response = await self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return Operation(**response)

    async def get_by_id(self, network_interface_group_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> NetworkInterfaceGroup:
        """
        (Provider) Gets a specific Network Interface Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_network_interface_group_by_id_with_http_info(network_interface_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str network_interface_group_id: (Provider) The Network Interface Group ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: NetworkInterfaceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/network-interface-groups/{network_interface_group_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{network_interface_group_id}", quote(str(network_interface_group_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return NetworkInterfaceGroup(**response)

    async def get(self, region_name: str, availability_zone_name: str, network_interface_group_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> NetworkInterfaceGroup:
        """
        (Provider) Gets a specific Network Interface Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_network_interface_group_with_http_info(region_name, availability_zone_name, network_interface_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str network_interface_group_name: (Provider) The Network Interface Group name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: NetworkInterfaceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/network-interface-groups/{network_interface_group_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{region_name}", quote(str(region_name), safe=""))
        url = url.replace("{availability_zone_name}", quote(str(availability_zone_name), safe=""))
        url = url.replace("{network_interface_group_name}", quote(str(network_interface_group_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return NetworkInterfaceGroup(**response)

    async def list(self, region_name: str, availability_zone_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> NetworkInterfaceGroupList:
        """
        (Provider) Gets a list of all Network Interface Groups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_network_interface_groups_with_http_info(region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: NetworkInterfaceGroupList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/network-interface-groups"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{region_name}", quote(str(region_name), safe=""))
        url = url.replace("{availability_zone_name}", quote(str(availability_zone_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return NetworkInterfaceGroupList(**response)

    async def update(self, network_interface_group: NetworkInterfaceGroupPatch, region_name: str, availability_zone_name: str, network_interface_group_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        (Provider) Updates a Network Interface Group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_network_interface_group_with_http_info(body, region_name, availability_zone_name, network_interface_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NetworkInterfaceGroupPatch body: (required)
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str network_interface_group_name: (Provider) The Network Interface Group name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/network-interface-groups/{network_interface_group_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id
        header_params["Content-Type"] = "application/json"

        query_params = []

        url = url.replace("{region_name}", quote(str(region_name), safe=""))
        url = url.replace("{availability_zone_name}", quote(str(availability_zone_name), safe=""))
        url = url.replace("{network_interface_group_name}", quote(str(network_interface_group_name), safe=""))
        response = await self.__client.patch(url, query_params, header_params, network_interface_group, timeout=timeout)
        
        return Operation(**response)
