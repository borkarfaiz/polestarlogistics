from django.db import models


class Ship(models.Model):
    imo_number = models.CharField(max_length=7, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Position(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    location = geomodels.PointField()

    def __str__(self):
        return f"{self.ship.name} - {self.timestamp}"
