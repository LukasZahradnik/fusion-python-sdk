from fusion.models.operation import Operation
from fusion.models.protection_policy_list import ProtectionPolicyList
from fusion.models.protection_policy import ProtectionPolicy
from fjuzn.http_client import HttpClient
from typing import Optional
from urllib.parse import quote

from fusion.models.protection_policy_post import ProtectionPolicyPost


class ProtectionPoliciesApi:
    __slots__ = "__client",
    
    def __init__(self, client: HttpClient):
        self.__client = client

    def create(self, protection_policy: ProtectionPolicyPost, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Creates a Protection Policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_protection_policy_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProtectionPolicyPost body: (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/protection-policies"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id
        header_params["Content-Type"] = "application/json"

        query_params = []

        
        response = self.__client.post(url, query_params, header_params, protection_policy, timeout=timeout)
        
        return Operation(**response)

    def delete(self, protection_policy_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Deletes a specific protection policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_protection_policy_with_http_info(protection_policy_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str protection_policy_name: The Protection Policy name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/protection-policies/{protection_policy_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{protection_policy_name}", quote(str(protection_policy_name), safe=""))
        response = self.__client.delete(url, query_params, header_params, timeout=timeout)
        
        return Operation(**response)

    def get_by_id(self, protection_policy_id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> ProtectionPolicy:
        """
        Gets a specific Protection Policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_protection_policy_by_id_with_http_info(protection_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str protection_policy_id: The Protection Policy ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: ProtectionPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/protection-policies/{protection_policy_id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{protection_policy_id}", quote(str(protection_policy_id), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return ProtectionPolicy(**response)

    def get(self, protection_policy_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> ProtectionPolicy:
        """
        Gets a specific Protection Policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_protection_policy_with_http_info(protection_policy_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str protection_policy_name: The Protection Policy name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: ProtectionPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/protection-policies/{protection_policy_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{protection_policy_name}", quote(str(protection_policy_name), safe=""))
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return ProtectionPolicy(**response)

    def list(self, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> ProtectionPolicyList:
        """
        Gets a list of all Protection Policies.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_protection_policies_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: ProtectionPolicyList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/protection-policies"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        
        response = self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return ProtectionPolicyList(**response)
