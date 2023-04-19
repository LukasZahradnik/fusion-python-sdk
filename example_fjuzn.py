import fusion
from fusion.models.region_post import RegionPost
from fusion.models.availability_zone_post import AvailabilityZonePost

from fjuzn import FusionClient


configuration = fusion.Configuration()

configuration.host = ""
configuration.issuer_id = ""
configuration.private_key_file = ""
configuration.token_endpoint = ""


def main():
    with FusionClient(configuration) as client:
        print("List all regions")
        regions = client.region.list()
        print(regions)

        print("Create new region")
        region_ref = client.region.create(RegionPost("my_new_region"))
        print(region_ref)
        
        print("Create az")
        az_ref = client.availability_zone.create(AvailabilityZonePost("my_new_az"), region_ref.name)
        print(az_ref)

        print("Create another region just because")
        another_region_ref = client.region.create(RegionPost("my_another_region"))
        
        print("List all regions") 
        regions = client.region.list()
        print(regions)
        
        print("Destroy all resources")
        client.availability_zone.delete(region_ref.name, az_ref.name)
        client.region.delete(region_ref.name)
        client.region.delete(another_region_ref.name)

        regions = client.region.list()
        print(regions)


main()
