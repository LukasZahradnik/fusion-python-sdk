from typing import Optional
from fusion.models.operation import Operation
from fjuzn.http_client import AsyncHttpClient
from fusion.models.storage_class_list import StorageClassList
from urllib.parse import quote

from fusion.models.storage_class_post import StorageClassPost
from fusion.models.storage_class import StorageClass
from fusion.models.storage_class_patch import StorageClassPatch


class StorageClassesApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def create(self, storage_class: StorageClassPost, storage_service_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        (Provider) Creates a Storage Class.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_storage_class_with_http_info(body, storage_service_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StorageClassPost body: (required)
        :param str storage_service_name: The Storage Service name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/storage-services/{storage_service_name}/storage-classes"
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
        response = await self.__client.post(url, query_params, header_params, storage_class, timeout=timeout)
        
        return Operation(**response)

    async def delete(self, storage_service_name: str, storage_class_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Deletes a Storage Class.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_storage_class_with_http_info(storage_service_name, storage_class_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str storage_service_name: The Storage Service name (required)
        :param str storage_class_name: The Storage Class name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/storage-services/{storage_service_name}/storage-classes/{storage_class_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{storage_service_name}", quote(str(storage_service_name), safe=""))
        url = url.replace("{storage_class_name}", quote(str(storage_class_name), safe=""))
        response = await self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return Operation(**response)

    async def get_by_id(self, storage_class_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> StorageClass:
        """
        Gets a specific Storage Class.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_storage_class_by_id_with_http_info(storage_class_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str storage_class_id: The Storage Class ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: StorageClass
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/storage-classes/{storage_class_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{storage_class_id}", quote(str(storage_class_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return StorageClass(**response)

    async def get(self, storage_service_name: str, storage_class_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> StorageClass:
        """
        Gets a specific Storage Class.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_storage_class_with_http_info(storage_service_name, storage_class_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str storage_service_name: The Storage Service name (required)
        :param str storage_class_name: The Storage Class name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: StorageClass
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/storage-services/{storage_service_name}/storage-classes/{storage_class_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{storage_service_name}", quote(str(storage_service_name), safe=""))
        url = url.replace("{storage_class_name}", quote(str(storage_class_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return StorageClass(**response)

    async def list(self, storage_service_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> StorageClassList:
        """
        Gets a list of all Storage Classes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_storage_classes_with_http_info(storage_service_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str storage_service_name: The Storage Service name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: StorageClassList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/storage-services/{storage_service_name}/storage-classes"
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
        
        return StorageClassList(**response)

    async def update(self, storage_class: StorageClassPatch, storage_service_name: str, storage_class_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Updates a Storage Class.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_storage_class_with_http_info(body, storage_service_name, storage_class_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StorageClassPatch body: (required)
        :param str storage_service_name: The Storage Service name (required)
        :param str storage_class_name: The Storage Class name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/storage-services/{storage_service_name}/storage-classes/{storage_class_name}"
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
        url = url.replace("{storage_class_name}", quote(str(storage_class_name), safe=""))
        response = await self.__client.patch(url, query_params, header_params, storage_class, timeout=timeout)
        
        return Operation(**response)
