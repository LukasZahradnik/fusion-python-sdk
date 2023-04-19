import asyncio

import fusion
from fusion.models.region_post import RegionPost
from fusion.models.availability_zone_post import AvailabilityZonePost

from fjuzn import AsyncFusionClient


configuration = fusion.Configuration()

configuration.host = ""
configuration.issuer_id = ""
configuration.private_key_file = ""
configuration.token_endpoint = ""


async def main():
    async with AsyncFusionClient(configuration) as client:
        print("List all regions")
        regions = await client.region.list()
        print(regions)

        print("Create new region")
        region_ref = await client.region.create(RegionPost("my_new_region"))
        print(region_ref)
        
        print("Create az")
        az_ref = await client.availability_zone.create(AvailabilityZonePost("my_new_az"), region_ref.name)
        print(az_ref)

        print("Create another region just because")
        another_region_ref = await client.region.create(RegionPost("my_another_region"))
        
        print("List all regions") 
        regions = await client.region.list()
        print(regions)
        
        print("Destroy all resources")
        await client.availability_zone.delete(region_ref.name, az_ref.name)
        await asyncio.gather(
            client.region.delete(region_ref.name),
            client.region.delete(another_region_ref.name),
        )

        regions = await client.region.list()
        print(regions)


asyncio.run(main())
