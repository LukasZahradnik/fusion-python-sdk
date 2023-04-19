from fusion.models.storage_endpoint import StorageEndpoint
from fusion.models.operation import Operation
from typing import Optional
from fjuzn.http_client import HttpClient
from fusion.models.storage_endpoint_patch import StorageEndpointPatch
from fusion.models.storage_endpoint_list import StorageEndpointList
from urllib.parse import quote

from fusion.models.storage_endpoint_post import StorageEndpointPost


class StorageEndpointsApi:
    __slots__ = "__client",
    
    def __init__(self, client: HttpClient):
        self.__client = client

    def create(self, storage_endpoint: StorageEndpointPost, region_name: str, availability_zone_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        (Provider) Creates a Storage Endpoint.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_storage_endpoint_with_http_info(body, region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StorageEndpointPost body: (required)
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/storage-endpoints"
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
        response = self.__client.post(url, query_params, header_params, storage_endpoint, timeout=timeout)
        
        return Operation(**response)

    def delete(self, region_name: str, availability_zone_name: str, storage_endpoint_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> None:
        """
        (Provider) Deletes a specific Storage Endpoint.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_storage_endpoint_with_http_info(region_name, availability_zone_name, storage_endpoint_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str storage_endpoint_name: (Provider) The Storage Endpoint name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/storage-endpoints/{storage_endpoint_name}"
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
        url = url.replace("{storage_endpoint_name}", quote(str(storage_endpoint_name), safe=""))
        response = self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return None

    def get_by_id(self, storage_endpoint_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> StorageEndpoint:
        """
        (Provider) Gets a specific Storage Endpoint.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_storage_endpoint_by_id_with_http_info(storage_endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str storage_endpoint_id: (Provider) The Storage Endpoint ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: StorageEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/storage-endpoints/{storage_endpoint_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{storage_endpoint_id}", quote(str(storage_endpoint_id), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return StorageEndpoint(**response)

    def get(self, region_name: str, availability_zone_name: str, storage_endpoint_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> StorageEndpoint:
        """
        (Provider) Gets a specific Storage Endpoint.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_storage_endpoint_with_http_info(region_name, availability_zone_name, storage_endpoint_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str storage_endpoint_name: (Provider) The Storage Endpoint name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: StorageEndpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/storage-endpoints/{storage_endpoint_name}"
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
        url = url.replace("{storage_endpoint_name}", quote(str(storage_endpoint_name), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return StorageEndpoint(**response)

    def list(self, region_name: str, availability_zone_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> StorageEndpointList:
        """
        (Provider) Gets a list of all Storage Endpoints.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_storage_endpoints_with_http_info(region_name, availability_zone_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: StorageEndpointList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/storage-endpoints"
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
        
        return StorageEndpointList(**response)

    def update(self, storage_endpoint: StorageEndpointPatch, region_name: str, availability_zone_name: str, storage_endpoint_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        (Provider) Updates a Storage Endpoint.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_storage_endpoint_with_http_info(body, region_name, availability_zone_name, storage_endpoint_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StorageEndpointPatch body: (required)
        :param str region_name: The Region name (required)
        :param str availability_zone_name: The Availability Zone name (required)
        :param str storage_endpoint_name: (Provider) The Storage Endpoint name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/regions/{region_name}/availability-zones/{availability_zone_name}/storage-endpoints/{storage_endpoint_name}"
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
        url = url.replace("{storage_endpoint_name}", quote(str(storage_endpoint_name), safe=""))
        response = self.__client.patch(url, query_params, header_params, storage_endpoint, timeout=timeout)
        
        return Operation(**response)
