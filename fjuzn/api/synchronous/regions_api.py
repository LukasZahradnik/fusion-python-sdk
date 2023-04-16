from fusion.models.region import Region
from fusion.models.region_patch import RegionPatch
from urllib.parse import quote

from fusion.models.region_ref import RegionRef
from typing import Optional
from fusion.models.region_post import RegionPost
from fusion.models.region_list import RegionList
from fjuzn.http_client import HttpClient


class RegionsApi:
    __slots__ = "__client",
    
    def __init__(self, client: HttpClient):
        self.__client = client

    def create(self, region: RegionPost, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> RegionRef:
        """
        Creates a Region.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_region_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RegionPost body: (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id
        header_params["Content-Type"] = "application/json"

        query_params = []

        
        response = self.__client.post(url, query_params, header_params, region, timeout=timeout)
        
        return RegionRef(**response)

    def delete(self, region_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> RegionRef:
        """
        Deletes a specific Region.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_region_with_http_info(region_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{region_name}", quote(str(region_name), safe=""))
        response = self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return RegionRef(**response)

    def get_by_id(self, region_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Region:
        """
        Gets a specific Region.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_region_by_id_with_http_info(region_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_id: The Region ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Region
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/regions/{region_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{region_id}", quote(str(region_id), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Region(**response)

    def get(self, region_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Region:
        """
        Gets a specific Region.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_region_with_http_info(region_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Region
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{region_name}", quote(str(region_name), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Region(**response)

    def list(self, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> RegionList:
        """
        Gets a list of all Regions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_regions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: RegionList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return RegionList(**response)

    def update(self, region: RegionPatch, region_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> RegionRef:
        """
        Updates a Region.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_region_with_http_info(body, region_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RegionPatch body: (required)
        :param str region_name: The Region name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}"
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
        response = self.__client.patch(url, query_params, header_params, region, timeout=timeout)
        
        return RegionRef(**response)
