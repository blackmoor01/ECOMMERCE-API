import csv
from tqdm import tqdm
from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Import products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            products = []
            for row in tqdm(reader):
                try:
                    products.append(Product(
                        name=row['name'],
                        description=row['description'],
                        price=row['price'],
                        stock=row['stock'],
                    ))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error: {e}'))
            Product.objects.bulk_create(products)
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))