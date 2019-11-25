from rest_framework import viewsets, filters

from .models import Farm, Tank, Device
from .serializers import FarmSerializer, TankSerializer, DeviceSerializer


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all().order_by('created_at')
    filter_backends = (filters.SearchFilter,)
    serializer_class = FarmSerializer


class TankViewSet(viewsets.ModelViewSet):
    queryset = Tank.objects.all().order_by('created_at')
    serializer_class = TankSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('created_at')
    serializer_class = DeviceSerializer
