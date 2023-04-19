from fusion.models.network_interface import NetworkInterface
from fusion.models.network_interface_ref import NetworkInterfaceRef
from urllib.parse import quote

from fjuzn.http_client import AsyncHttpClient
from typing import Optional
from fusion.models.network_interface_patch import NetworkInterfacePatch
from fusion.models.network_interface_list import NetworkInterfaceList


class NetworkInterfacesApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def get_by_id(self, network_interface_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> NetworkInterface:
        """
        (Provider) Gets a specific Network Interface.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_network_interface_by_id_with_http_info(network_interface_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str network_interface_id: (Provider) The Network Interface ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: NetworkInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/network-interfaces/{network_interface_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{network_interface_id}", quote(str(network_interface_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return NetworkInterface(**response)

    async def get(self, region_name: str, availability_zone_name: str, array_name: str, net_intf_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> NetworkInterface:
        """
        (Provider) Gets a specific Network Interface.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_network_interface_with_http_info(region_name, availability_zone_name, array_name, net_intf_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str array_name: The Array name (required)
        :param str net_intf_name: (Provider) The Network Interface name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: NetworkInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/arrays/{array_name}/network-interfaces/{net_intf_name}"
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
        url = url.replace("{array_name}", quote(str(array_name), safe=""))
        url = url.replace("{net_intf_name}", quote(str(net_intf_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return NetworkInterface(**response)

    async def list(self, region_name: str, availability_zone_name: str, array_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> NetworkInterfaceList:
        """
        (Provider) Gets a list of all Network Interfaces.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_network_interfaces_with_http_info(region_name, availability_zone_name, array_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str array_name: The Array name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: NetworkInterfaceList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/arrays/{array_name}/network-interfaces"
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
        url = url.replace("{array_name}", quote(str(array_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return NetworkInterfaceList(**response)

    async def update(self, network_interface: NetworkInterfacePatch, region_name: str, availability_zone_name: str, array_name: str, net_intf_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> NetworkInterfaceRef:
        """
        (Provider) Updates a Network Interface.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_network_interface_with_http_info(body, region_name, availability_zone_name, array_name, net_intf_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NetworkInterfacePatch body: (required)
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str array_name: The Array name (required)
        :param str net_intf_name: (Provider) The Network Interface name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/arrays/{array_name}/network-interfaces/{net_intf_name}"
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
        url = url.replace("{array_name}", quote(str(array_name), safe=""))
        url = url.replace("{net_intf_name}", quote(str(net_intf_name), safe=""))
        response = await self.__client.patch(url, query_params, header_params, network_interface, timeout=timeout)
        
        return NetworkInterfaceRef(**response)
