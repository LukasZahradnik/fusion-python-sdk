from urllib.parse import quote

from fusion.models.array_list import ArrayList
from typing import Optional
from fusion.models.array_ref import ArrayRef
from fusion.models.array_post import ArrayPost
from fusion.models.space import Space
from fusion.models.array import Array
from fusion.models.array_patch import ArrayPatch
from fusion.models.performance import Performance
from fjuzn.http_client import AsyncHttpClient


class ArraysApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def create(self, array: ArrayPost, region_name: str, availability_zone_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> ArrayRef:
        """
        (Provider) Registers an array into Pure Fusion.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_array_with_http_info(body, region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ArrayPost body: (required)
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/arrays"
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
        response = await self.__client.post(url, query_params, header_params, array, timeout=timeout)
        
        return ArrayRef(**response)

    async def delete(self, region_name: str, availability_zone_name: str, array_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> ArrayRef:
        """
        Deregister a specific array.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_array_with_http_info(region_name, availability_zone_name, array_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str array_name: The Array name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/arrays/{array_name}"
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
        response = await self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return ArrayRef(**response)

    async def get_by_id(self, array_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Array:
        """
        (Provider) Gets a specific Array.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_array_by_id_with_http_info(array_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str array_id: The Array ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Array
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/arrays/{array_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{array_id}", quote(str(array_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Array(**response)

    async def get_performance(self, region_name: str, availability_zone_name: str, array_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Performance:
        """
        (Provider) Gets performance metrics of a specific Array.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_array_performance_with_http_info(region_name, availability_zone_name, array_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str array_name: The Array name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Performance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/arrays/{array_name}/performance"
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
        
        return Performance(**response)

    async def get_space(self, region_name: str, availability_zone_name: str, array_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Space:
        """
        (Provider) Gets performance metrics of a specific Array.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_array_space_with_http_info(region_name, availability_zone_name, array_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str array_name: The Array name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/arrays/{array_name}/space"
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
        
        return Space(**response)

    async def get(self, region_name: str, availability_zone_name: str, array_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Array:
        """
        (Provider) Gets a specific Array.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_array_with_http_info(region_name, availability_zone_name, array_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str array_name: The Array name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Array
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/arrays/{array_name}"
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
        
        return Array(**response)

    async def list(self, region_name: str, availability_zone_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> ArrayList:
        """
        (Provider) Gets a list of all arrays registered to Pure Fusion.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_arrays_with_http_info(region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: ArrayList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/arrays"
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
        
        return ArrayList(**response)

    async def update(self, array: ArrayPatch, region_name: str, availability_zone_name: str, array_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> ArrayRef:
        """
        Updates a specific array.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_array_with_http_info(body, region_name, availability_zone_name, array_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ArrayPatch body: (required)
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str array_name: The Array name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/arrays/{array_name}"
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
        response = await self.__client.patch(url, query_params, header_params, array, timeout=timeout)
        
        return ArrayRef(**response)
