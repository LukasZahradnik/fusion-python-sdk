from fusion.models.api_client import APIClient
from fusion.models.user import User
from urllib.parse import quote

from typing import List
from fjuzn.http_client import AsyncHttpClient
from typing import Optional
from fusion.models.api_client_post import APIClientPost


class IdentityManagerApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def create_api_client(self, identity_manage: APIClientPost, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> APIClient:
        """
        Creates an API Client  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_api_client_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param APIClientPost body: (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: APIClient
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/api-clients"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id
        header_params["Content-Type"] = "application/json"

        query_params = []

        
        response = await self.__client.post(url, query_params, header_params, identity_manage, timeout=timeout)
        
        return APIClient(**response)

    async def delete_api_client(self, api_client_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> APIClient:
        """
        Deletes a specific API Client  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_api_client_with_http_info(api_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_client_id: The API Client ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: APIClient
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/api-clients/{api_client_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{api_client_id}", quote(str(api_client_id), safe=""))
        response = await self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return APIClient(**response)

    async def get_api_client_by_id(self, api_client_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> APIClient:
        """
        Gets a specific API Client  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_client_by_id_with_http_info(api_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_client_id: The API Client ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: APIClient
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/api-clients/{api_client_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{api_client_id}", quote(str(api_client_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return APIClient(**response)

    async def get_api_client(self, api_client_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> APIClient:
        """
        Gets a specific API Client  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_client_with_http_info(api_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_client_id: The API Client ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: APIClient
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/api-clients/{api_client_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{api_client_id}", quote(str(api_client_id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return APIClient(**response)

    async def list_api_clients(self, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> List[APIClient]:
        """
        Gets a list of all API Clients  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_api_clients_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: list[APIClient]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/api-clients"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return [APIClient(**r) for r in response]

    async def list_users(self, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, name: Optional[str] = None, email: Optional[str] = None, timeout: Optional[float] = None) -> List[User]:
        """
        Gets a list of all users.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_users_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :param str name:
        :param str email:
        :return: list[User]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/users"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []
        if name is not None:
            query_params.append(("name", name))
        if email is not None:
            query_params.append(("email", email))

        
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return [User(**r) for r in response]