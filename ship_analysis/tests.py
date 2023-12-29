from django.contrib.gis.geos import Point
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Ship, Position


class ShipModelTests(TestCase):

    def setUp(self):
        Ship.objects.create(imo_number='1234567', name='Test Ship')

    def test_ship_creation(self):
        ship = Ship.objects.get(imo_number='1234567')
        self.assertEqual(ship.name, 'Test Ship')


class PositionModelTests(TestCase):

    def setUp(self):
        ship = Ship.objects.create(imo_number='1234567', name='Test Ship')
        Position.objects.create(
            ship=ship,
            location=Point(1.0, 1.0),
            timestamp='2021-01-01T00:00:00Z'
        )

    def test_position_creation(self):
        ship = Ship.objects.get(imo_number='1234567')
        position = Position.objects.get(ship=ship)
        self.assertEqual(position.location.x, 1.0)
        self.assertEqual(position.location.y, 1.0)


class ShipAPITests(APITestCase):

    def setUp(self):
        self.ship = Ship.objects.create(imo_number='1234567', name='Test Ship')

    def test_get_ships(self):
        url = reverse('ship-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only have one ship in setUp
        self.assertEqual(response.json()[0], {"imo_number": "1234567", "name": "Test Ship"})


class PositionAPITests(APITestCase):

    def setUp(self):
        self.ship = Ship.objects.create(imo_number='1234567', name='Test Ship')
        Position.objects.create(
            ship=self.ship,
            location=Point(1.0, 1.0),
            timestamp='2021-01-01T00:00:00Z'
        )

    def test_get_positions(self):
        url = reverse('position-list', kwargs={'imo': self.ship.imo_number})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            {'location': 'SRID=4326;POINT (1 1)', 'timestamp': '2021-01-01T00:00:00Z'}, response.json()[0]
        )
