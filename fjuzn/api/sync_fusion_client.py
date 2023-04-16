from typing import Optional

import httpx

from fjuzn.api.synchronous.arrays_api import ArraysApi
from fjuzn.api.synchronous.availability_zones_api import AvailabilityZonesApi
from fjuzn.api.synchronous.hardware_types_api import HardwareTypesApi
from fjuzn.api.synchronous.host_access_policies_api import HostAccessPoliciesApi
from fjuzn.api.synchronous.identity_manager_api import IdentityManagerApi
from fjuzn.api.synchronous.network_interface_groups_api import NetworkInterfaceGroupsApi
from fjuzn.api.synchronous.network_interfaces_api import NetworkInterfacesApi
from fjuzn.api.synchronous.operations_api import OperationsApi
from fjuzn.api.synchronous.placement_groups_api import PlacementGroupsApi
from fjuzn.api.synchronous.protection_policies_api import ProtectionPoliciesApi
from fjuzn.api.synchronous.regions_api import RegionsApi
from fjuzn.api.synchronous.role_assignments_api import RoleAssignmentsApi
from fjuzn.api.synchronous.roles_api import RolesApi
from fjuzn.api.synchronous.snapshots_api import SnapshotsApi
from fjuzn.api.synchronous.storage_classes_api import StorageClassesApi
from fjuzn.api.synchronous.storage_endpoints_api import StorageEndpointsApi
from fjuzn.api.synchronous.storage_services_api import StorageServicesApi
from fjuzn.api.synchronous.tenant_spaces_api import TenantSpacesApi
from fjuzn.api.synchronous.tenants_api import TenantsApi
from fjuzn.api.synchronous.volume_snapshots_api import VolumeSnapshotsApi
from fjuzn.api.synchronous.volumes_api import VolumesApi
from fjuzn.api.synchronous.workload_planner_api import WorkloadPlannerApi
from fjuzn.api.synchronous.default_api import DefaultApi

from fjuzn.http_client import HttpClient


class FusionClient:
    __slots__ = "__client",

    def __init__(self):
        self.__client: Optional[HttpClient] = None

    def __enter__(self):
        self.__client = HttpClient(httpx.Client())
        self.__client.client.__enter__()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__client.client.__exit__()

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

