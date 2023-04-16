from fusion.models.host_access_policies_post import HostAccessPoliciesPost
from fusion.models.operation import Operation
from fjuzn.http_client import HttpClient
from fusion.models.host_access_policy_list import HostAccessPolicyList
from typing import Optional
from urllib.parse import quote

from fusion.models.host_access_policy import HostAccessPolicy


class HostAccessPoliciesApi:
    __slots__ = "__client",
    
    def __init__(self, client: HttpClient):
        self.__client = client

    def create(self, host_access_policy: HostAccessPoliciesPost, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Creates a Host Access Policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_host_access_policy_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HostAccessPoliciesPost body: (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/host-access-policies"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id
        header_params["Content-Type"] = "application/json"

        query_params = []

        
        response = self.__client.post(url, query_params, header_params, host_access_policy, timeout=timeout)
        
        return Operation(**response)

    def delete(self, host_access_policy_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Deletes a specific host access policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_host_access_policy_with_http_info(host_access_policy_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str host_access_policy_name: The Host policy name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/host-access-policies/{host_access_policy_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{host_access_policy_name}", quote(str(host_access_policy_name), safe=""))
        response = self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return Operation(**response)

    def get_by_id(self, host_access_policy_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> HostAccessPolicy:
        """
        Gets a specific Host Access Policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_host_access_policy_by_id_with_http_info(host_access_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str host_access_policy_id: The Host policy ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: HostAccessPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/host-access-policies/{host_access_policy_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{host_access_policy_id}", quote(str(host_access_policy_id), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return HostAccessPolicy(**response)

    def get(self, host_access_policy_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> HostAccessPolicy:
        """
        Gets a specific Host Access Policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_host_access_policy_with_http_info(host_access_policy_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str host_access_policy_name: The Host policy name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: HostAccessPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/host-access-policies/{host_access_policy_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{host_access_policy_name}", quote(str(host_access_policy_name), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return HostAccessPolicy(**response)

    def list(self, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> HostAccessPolicyList:
        """
        Gets a list of all Host Access Policies.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_host_access_policies_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: HostAccessPolicyList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/host-access-policies"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return HostAccessPolicyList(**response)
