import csv
from django.core.management.base import BaseCommand
from searchapp.models import Restaurant

class Command(BaseCommand):
    help = 'Load restaurant data from CSV'

    def handle(self, *args, **kwargs):
        csv_file = 'searchapp/static/csv/restaurants_small.csv'  # Path to your CSV file
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Restaurant.objects.create(
                    id=row['id'],
                    name=row['name'],
                    location=row['location'],
                    items=row['items'],
                    lat_long=row['lat_long'],
                    full_details=row['full_details']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from CSV'))
