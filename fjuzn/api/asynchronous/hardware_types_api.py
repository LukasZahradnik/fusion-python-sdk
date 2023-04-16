from fusion.models.hardware_type import HardwareType
from typing import Optional
from fjuzn.http_client import AsyncHttpClient
from urllib.parse import quote

from fusion.models.hardware_type_list import HardwareTypeList


class HardwareTypesApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def get_by_id(self, hardware_type_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> HardwareType:
        """
        (Provider) Gets a specific Hardware Type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hardware_type_by_id_with_http_info(hardware_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hardware_type_id: (Provider) The Hardware Type ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: HardwareType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/hardware-types/{hardware_type_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{hardware_type_id}", quote(str(hardware_type_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return HardwareType(**response)

    async def get(self, hardware_type_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> HardwareType:
        """
        (Provider) Gets a specific Hardware Type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hardware_type_with_http_info(hardware_type_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hardware_type_name: (Provider) The Hardware Type name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: HardwareType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/hardware-types/{hardware_type_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{hardware_type_name}", quote(str(hardware_type_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return HardwareType(**response)

    async def list(self, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, media_type: Optional[str] = None, array_type: Optional[str] = None, timeout: Optional[float] = None) -> HardwareTypeList:
        """
        (Provider) Gets a list of all hardware types.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_hardware_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :param str media_type: Return only hardware types matching the given media type
        :param str array_type: Return only hardware types matching the given array type
        :return: HardwareTypeList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/hardware-types"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []
        if media_type is not None:
            query_params.append(("mediaType", media_type))
        if array_type is not None:
            query_params.append(("arrayType", array_type))

        
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return HardwareTypeList(**response)
