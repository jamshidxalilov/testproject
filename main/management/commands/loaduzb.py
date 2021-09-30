import requests
from django.core.management.base import BaseCommand
from main.models import Country, Region, District
IMPORT_URL = 'https://opendata.gov.uz/uz/datasets/download/3395/json'


class Command(BaseCommand):
    def import_data(self, json_data):
        regions = []
        districts = []
        region_codes = ["1703", "1706", "1708", "1710", "1712", "1714", "1718", "1722", "1724", "1726", "1727", "1730",
                        "1733", "1735"]

        for data in json_data:
            if data['id'] == '1':
                name = data['G2']
                Country.objects.create(name=name).save()

            for code in region_codes:
                if data['G1'] == code:
                    regions.append(Region(name=data['G2'], country_id=1))

            for id, code in enumerate(region_codes):
                if data['G1'][:4] == code:
                    districts.append(District(country_id=1, region_id=id+1, name=data['G2']))

        Region.objects.bulk_create(regions)
        District.objects.bulk_create(districts)

    def handle(self, *args, **options):
        response = requests.get(IMPORT_URL)
        json_data = response.json()

        data = []
        for d in json_data:
            data.append(d)

        self.import_data(data)