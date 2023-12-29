import csv
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from ship_analysis.models import Ship, Position


class Command(BaseCommand):
    help = 'Imports data from CSV into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        ship_mappings = {
            "9632179": "Mathilde Maersk",
            "9247455": "Australian Spirit",
            "9595321": "MSC Preziosa",
        }

        # ships = [Ship(imo_number=key, name=value) for key, value in ship_mappings.items()]
        # Ship.objects.bulk_create(ships)
        for key, value in ship_mappings.items():
            Ship.objects.get_or_create(imo_number=key, name=value)
        ship_object_mappings = {
            imo_number: Ship.objects.get(imo_number=imo_number) for imo_number in ship_mappings.keys()
        }
        with open(csv_file, newline='') as file:
            reader = csv.reader(file)
            positions = [
                Position(
                    ship=ship_object_mappings.get(row[0]),
                    location=Point(float(row[2]), float(row[3])),
                    timestamp=row[1])
                for row in reader]
        Position.objects.bulk_create(positions)
        self.stdout.write(self.style.SUCCESS('Successfully imported'))
