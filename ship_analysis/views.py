from django.shortcuts import render

from rest_framework import generics

from .models import Ship, Position
from .serializers import ShipSerializer, PositionSerializer


def index(request):
    return render(request, 'index.html')


class ShipList(generics.ListAPIView):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class PositionList(generics.ListAPIView):
    serializer_class = PositionSerializer

    def get_queryset(self):
        imo_number = self.kwargs['imo']
        return Position.objects.filter(ship__imo_number=imo_number).order_by('-timestamp')
