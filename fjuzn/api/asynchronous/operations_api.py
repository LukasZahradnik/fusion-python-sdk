from urllib.parse import quote

from fjuzn.http_client import AsyncHttpClient
from typing import Optional
from fusion.models.operation_list import OperationList
from fusion.models.operation import Operation


class OperationsApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def get_by_id(self, id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Gets a specific Operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operation_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Operation ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/resources/operations/{id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{id}", quote(str(id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Operation(**response)

    async def get(self, id: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> Operation:
        """
        Gets a specific Operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operation_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Operation ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/operations/{id}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{id}", quote(str(id), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return Operation(**response)

    async def list(self, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, action: Optional[str] = None, request_id: Optional[str] = None, request_collection: Optional[str] = None, resource_kind: Optional[str] = None, resource_id: Optional[str] = None, status: Optional[str] = None, created_after: Optional[str] = None, filter: Optional[str] = None, sort: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, timeout: Optional[float] = None) -> OperationList:
        """
        Gets a list of Operations matching the criteria.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_operations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :param str action: The action requested.
        :param str request_id: The request ID supplied with the request.
        :param str request_collection: Default to \"/\", valid values take the form \"/\", \"/tenants/<tname>\", or \"/tenants/<tname>/tenant-spaces/<tsname>\"
        :param str resource_kind: The kind of resource on which the Operation was performed.
        :param str resource_id: The ID of resource on which the Operation was performed.
        :param str status: The status of the Operation. Support for comma separated multiple status is deprecated, use IN list instead
        :param str created_after:
        :param str filter: filter should use expression language for filtering
        :param str sort: Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. "sort=size-,name")
        :param int limit:
        :param int offset:
        :return: OperationList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/operations"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []
        if action is not None:
            query_params.append(("action", action))
        if request_id is not None:
            query_params.append(("request_id", request_id))
        if request_collection is not None:
            query_params.append(("request_collection", request_collection))
        if resource_kind is not None:
            query_params.append(("resource_kind", resource_kind))
        if resource_id is not None:
            query_params.append(("resource_id", resource_id))
        if status is not None:
            query_params.append(("status", status))
        if created_after is not None:
            query_params.append(("created_after", created_after))
        if filter is not None:
            query_params.append(("filter", filter))
        if sort is not None:
            query_params.append(("sort", sort))
        if limit is not None:
            query_params.append(("limit", limit))
        if offset is not None:
            query_params.append(("offset", offset))

        
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return OperationList(**response)
