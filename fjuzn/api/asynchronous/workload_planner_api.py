from urllib.parse import quote

from typing import Optional
from fusion.models.placement_recommendation_post import PlacementRecommendationPost
from fusion.models.placement_recommendation import PlacementRecommendation
from fusion.models.workload_planne_ref import WorkloadPlanneRef
from fjuzn.http_client import AsyncHttpClient


class WorkloadPlannerApi:
    __slots__ = "__client",
    
    def __init__(self, client: AsyncHttpClient):
        self.__client = client

    async def create_placement_recommendation(self, workload_planne: PlacementRecommendationPost, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> WorkloadPlanneRef:
        """
        (Provider) Generates a report on the candidate arrays a given placement group can be placed/migrated to  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_placement_recommendation_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PlacementRecommendationPost body: (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/workload-planner/placement-recommendations"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id
        header_params["Content-Type"] = "application/json"

        query_params = []

        
        response = await self.__client.post(url, query_params, header_params, workload_planne, timeout=timeout)
        
        return WorkloadPlanneRef(**response)

    async def get_placement_recommendation(self, placement_recommendation_name: str, *, x_request_id: Optional[str] = None, authorization: Optional[str] = None, x_correlation_id: Optional[str] = None, timeout: Optional[float] = None) -> PlacementRecommendation:
        """
        Gets a specific placement recommendation report  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_placement_recommendation_with_http_info(placement_recommendation_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str placement_recommendation_name: Name of Placement Recommendation report (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: PlacementRecommendation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        url = "/workload-planner/placement-recommendations/{placement_recommendation_name}"
        header_params = {"Accept": "application/json"}
        if x_request_id is not None:
            header_params["X-Request-ID"] = x_request_id
        if authorization is not None:
            header_params["Authorization"] = authorization
        if x_correlation_id is not None:
            header_params["X-Correlation-ID"] = x_correlation_id

        query_params = []

        url = url.replace("{placement_recommendation_name}", quote(str(placement_recommendation_name), safe=""))
        response = await self.__client.get(url, query_params, header_params, timeout=timeout)
        
        return PlacementRecommendation(**response)
