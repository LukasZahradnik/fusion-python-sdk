import fusion
from fusion.models.region_post import RegionPost
from fusion.models.availability_zone_post import AvailabilityZonePost


configuration = fusion.Configuration()

configuration.host = ""
configuration.issuer_id = ""
configuration.private_key_file = ""
configuration.token_endpoint = ""


from examples.util import wait_operation_finish

def main():
    # create an instance of the API class
    api_client = fusion.ApiClient(configuration)

    region_client = fusion.RegionsApi(api_client)
    az_client = fusion.AvailabilityZonesApi(api_client)

    print("List all regions")
    regions = region_client.list_regions()
    print(regions)

    op = region_client.delete_region("my_new_region")
    wait_operation_finish(op.id, api_client)

    print("Create new region")
    op = region_client.create_region(RegionPost("my_new_region"))
    region_ref = wait_operation_finish(op.id, api_client).result.resource
    print(region_ref)
    
    print("Create az")
    op = az_client.create_availability_zone(AvailabilityZonePost("my_new_az"), region_ref.name)
    az_ref = wait_operation_finish(op.id, api_client).result.resource
    print(az_ref)

    print("Create another region just because")
    op = region_client.create_region(RegionPost("my_another_region"))
    another_region_ref = wait_operation_finish(op.id, api_client).result.resource
    
    print("List all regions") 
    regions = region_client.list_regions()
    print(regions)
    
    print("Destroy all resources")
    op = az_client.delete_availability_zone(region_ref.name, az_ref.name)
    wait_operation_finish(op.id, api_client)

    op = region_client.delete_region(region_ref.name)
    wait_operation_finish(op.id, api_client)

    op = region_client.delete_region(another_region_ref.name)
    wait_operation_finish(op.id, api_client)

    regions = region_client.list_regions()
    print(regions)

main()
