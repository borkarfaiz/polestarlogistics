from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/ships/', views.ShipList.as_view(), name='ship-list'),
    path('api/positions/<str:imo>/', views.PositionList.as_view(), name='position-list'),
]
