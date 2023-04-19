from typing import Optional
from fjuzn.http_client import HttpClient
from fusion.models.version import Version
from urllib.parse import quote



class DefaultApi:
    __slots__ = "__client",
    
    def __init__(self, client: HttpClient):
        self.__client = client

    def get_version(self, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Version:
        """
        Gets the version of the Pure Fusion control plane.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_version_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Version
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/info/version"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Version(**response)
