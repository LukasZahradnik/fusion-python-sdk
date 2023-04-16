from fusion.models.storage_service_list import StorageServiceList
from typing import Optional
from fusion.models.operation import Operation
from fjuzn.http_client import AsyncHttpClient
from urllib.parse import quote

from fusion.models.storage_service import StorageService
from fusion.models.storage_service_patch import StorageServicePatch
from fusion.models.storage_service_post import StorageServicePost


class StorageServicesApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def create(self, storage_service: StorageServicePost, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        (Provider) Creates a Storage Service.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_storage_service_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StorageServicePost body: (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/storage-services"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id
        header_params["Content-Type"] = "application/json"

        query_params = []

        
        response = await self.__client.post(url, query_params, header_params, storage_service, timeout=timeout)
        
        return Operation(**response)

    async def delete(self, storage_service_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        (Provider) Deletes a Storage Service.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_storage_service_with_http_info(storage_service_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str storage_service_name: The Storage Service name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/storage-services/{storage_service_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{storage_service_name}", quote(str(storage_service_name), safe=""))
        response = await self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return Operation(**response)

    async def get_by_id(self, storage_service_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> StorageService:
        """
        Gets a specific Storage Service.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_storage_service_by_id_with_http_info(storage_service_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str storage_service_id: The Storage Service ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: StorageService
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/storage-services/{storage_service_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{storage_service_id}", quote(str(storage_service_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return StorageService(**response)

    async def get(self, storage_service_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> StorageService:
        """
        Gets a specific Storage Service.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_storage_service_with_http_info(storage_service_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str storage_service_name: The Storage Service name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: StorageService
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/storage-services/{storage_service_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{storage_service_name}", quote(str(storage_service_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return StorageService(**response)

    async def list(self, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> StorageServiceList:
        """
        Gets a list of all Storage Services.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_storage_services_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: StorageServiceList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/storage-services"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return StorageServiceList(**response)

    async def update(self, storage_service: StorageServicePatch, storage_service_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        (Provider) Updates a Storage Service.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_storage_service_with_http_info(body, storage_service_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StorageServicePatch body: (required)
        :param str storage_service_name: The Storage Service name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/storage-services/{storage_service_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id
        header_params["Content-Type"] = "application/json"

        query_params = []

        url = url.replace("{storage_service_name}", quote(str(storage_service_name), safe=""))
        response = await self.__client.patch(url, query_params, header_params, storage_service, timeout=timeout)
        
        return Operation(**response)
