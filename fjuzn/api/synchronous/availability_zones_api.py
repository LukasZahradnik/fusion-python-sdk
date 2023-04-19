from fusion.models.availability_zone_list import AvailabilityZoneList
from fusion.models.availability_zone_post import AvailabilityZonePost
from typing import Optional
from fusion.models.availability_zone_ref import AvailabilityZoneRef
from fjuzn.http_client import HttpClient
from fusion.models.availability_zone import AvailabilityZone
from urllib.parse import quote

from fusion.models.performance import Performance
from fusion.models.space import Space


class AvailabilityZonesApi:
    __slots__ = "__client",
    
    def __init__(self, client: HttpClient):
        self.__client = client

    def create(self, availability_zone: AvailabilityZonePost, region_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> AvailabilityZoneRef:
        """
        Creates an Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_availability_zone_with_http_info(body, region_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AvailabilityZonePost body: (required)
        :param str region_name: The Region name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones"
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
        response = self.__client.post(url, query_params, header_params, availability_zone, timeout=timeout)
        
        return AvailabilityZoneRef(**response)

    def delete(self, region_name: str, availability_zone_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> None:
        """
        Deletes a specific Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_availability_zone_with_http_info(region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}"
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
        response = self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return None

    def get_by_id(self, availability_zone_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> AvailabilityZone:
        """
        Gets a specific Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_availability_zone_by_id_with_http_info(availability_zone_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str availability_zone_id: The Availability Zone ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: AvailabilityZone
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/availability-zones/{availability_zone_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{availability_zone_id}", quote(str(availability_zone_id), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return AvailabilityZone(**response)

    def get_performance(self, region_name: str, availability_zone_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Performance:
        """
        (Provider) Gets performance metrics of a specific Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_availability_zone_performance_with_http_info(region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Performance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/performance"
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
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Performance(**response)

    def get_space(self, region_name: str, availability_zone_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Space:
        """
        (Provider) Gets space metrics of a specific Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_availability_zone_space_with_http_info(region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Space
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/space"
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
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Space(**response)

    def get(self, region_name: str, availability_zone_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> AvailabilityZone:
        """
        Gets a specific Availability Zone.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_availability_zone_with_http_info(region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: AvailabilityZone
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}"
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
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return AvailabilityZone(**response)

    def list(self, region_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> AvailabilityZoneList:
        """
        Gets a list of all Availability Zones.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_availability_zones_with_http_info(region_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: AvailabilityZoneList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones"
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
        
        return AvailabilityZoneList(**response)
