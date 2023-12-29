from rest_framework import serializers
from .models import Ship, Position


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ['imo_number', 'name']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['location', 'timestamp']
