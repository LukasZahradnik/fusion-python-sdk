from typing import Optional

import httpx

from fjuzn.api.asynchronous.arrays_api import ArraysApi
from fjuzn.api.asynchronous.availability_zones_api import AvailabilityZonesApi
from fjuzn.api.asynchronous.hardware_types_api import HardwareTypesApi
from fjuzn.api.asynchronous.host_access_policies_api import HostAccessPoliciesApi
from fjuzn.api.asynchronous.identity_manager_api import IdentityManagerApi
from fjuzn.api.asynchronous.network_interface_groups_api import NetworkInterfaceGroupsApi
from fjuzn.api.asynchronous.network_interfaces_api import NetworkInterfacesApi
from fjuzn.api.asynchronous.operations_api import OperationsApi
from fjuzn.api.asynchronous.placement_groups_api import PlacementGroupsApi
from fjuzn.api.asynchronous.protection_policies_api import ProtectionPoliciesApi
from fjuzn.api.asynchronous.regions_api import RegionsApi
from fjuzn.api.asynchronous.role_assignments_api import RoleAssignmentsApi
from fjuzn.api.asynchronous.roles_api import RolesApi
from fjuzn.api.asynchronous.snapshots_api import SnapshotsApi
from fjuzn.api.asynchronous.storage_classes_api import StorageClassesApi
from fjuzn.api.asynchronous.storage_endpoints_api import StorageEndpointsApi
from fjuzn.api.asynchronous.storage_services_api import StorageServicesApi
from fjuzn.api.asynchronous.tenant_spaces_api import TenantSpacesApi
from fjuzn.api.asynchronous.tenants_api import TenantsApi
from fjuzn.api.asynchronous.volume_snapshots_api import VolumeSnapshotsApi
from fjuzn.api.asynchronous.volumes_api import VolumesApi
from fjuzn.api.asynchronous.workload_planner_api import WorkloadPlannerApi
from fjuzn.api.asynchronous.default_api import DefaultApi

from fjuzn.http_client import AsyncHttpClient


class AsyncFusionClient:
    __slots__ = "__client", "__configuration"

    def __init__(self, configuration):
        self.__client: Optional[AsyncHttpClient] = None
        self.__configuration = configuration

    async def __aenter__(self):
        settings = self.__configuration.auth_settings()
        headers = {
            settings["oauth"]["key"]: settings["oauth"]["value"],
            "User-Agent": "Swagger-Codegen/1.0.11/python",    
        }

        self.__client = AsyncHttpClient(httpx.AsyncClient(base_url=self.__configuration.host), headers)
        await self.__client.client.__aenter__()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.__client.client.__aexit__()

    @property
    def array(self) -> ArraysApi:
        return ArraysApi(self.__client)

    @property
    def availability_zone(self) -> AvailabilityZonesApi:
        return AvailabilityZonesApi(self.__client)

    @property
    def hardware_type(self) -> HardwareTypesApi:
        return HardwareTypesApi(self.__client)

    @property
    def host_access_policy(self) -> HostAccessPoliciesApi:
        return HostAccessPoliciesApi(self.__client)

    @property
    def identity_manager(self) -> IdentityManagerApi:
        return IdentityManagerApi(self.__client)

    @property
    def network_interface_group(self) -> NetworkInterfaceGroupsApi:
        return NetworkInterfaceGroupsApi(self.__client)

    @property
    def network_interface(self) -> NetworkInterfacesApi:
        return NetworkInterfacesApi(self.__client)

    @property
    def operation(self) -> OperationsApi:
        return OperationsApi(self.__client)

    @property
    def placement_group(self) -> PlacementGroupsApi:
        return PlacementGroupsApi(self.__client)

    @property
    def protection_policy(self) -> ProtectionPoliciesApi:
        return ProtectionPoliciesApi(self.__client)

    @property
    def region(self) -> RegionsApi:
        return RegionsApi(self.__client)

    @property
    def role_assignment(self) -> RoleAssignmentsApi:
        return RoleAssignmentsApi(self.__client)

    @property
    def role(self) -> RolesApi:
        return RolesApi(self.__client)

    @property
    def snapshot(self) -> SnapshotsApi:
        return SnapshotsApi(self.__client)

    @property
    def storage_class(self) -> StorageClassesApi:
        return StorageClassesApi(self.__client)

    @property
    def storage_endpoint(self) -> StorageEndpointsApi:
        return StorageEndpointsApi(self.__client)

    @property
    def storage_service(self) -> StorageServicesApi:
        return StorageServicesApi(self.__client)

    @property
    def tenant_space(self) -> TenantSpacesApi:
        return TenantSpacesApi(self.__client)

    @property
    def tenant(self) -> TenantsApi:
        return TenantsApi(self.__client)

    @property
    def volume_snapshots(self) -> VolumeSnapshotsApi:
        return VolumeSnapshotsApi(self.__client)

    @property
    def workload_planner(self) -> WorkloadPlannerApi:
        return WorkloadPlannerApi(self.__client)

    @property
    def default(self) -> DefaultApi:
        return DefaultApi(self.__client)

    @property
    def volume(self) -> VolumesApi:
        return VolumesApi(self.__client)

