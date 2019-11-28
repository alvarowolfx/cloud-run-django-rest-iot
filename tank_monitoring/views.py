from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Farm, Tank, Device
from .services import DeviceTelemetry
from .serializers import FarmSerializer, TankSerializer, DeviceSerializer, DeviceTeletrySerializer, DeviceTeletryHistorySerializer


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

    @action(detail=False, methods=['post'])
    def telemetry(self, request):
        serializer = DeviceTeletrySerializer(data=request.data)
        if serializer.is_valid():
            device_id = serializer.data['device_id']
            data = serializer.data
            del data['device_id']

            device, created = Device.objects.get_or_create(deviceId=device_id,)
            device_id = device.id
            DeviceTelemetry().save(device_id, data)
            return Response({
                "message": "OK"
            })
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def history(self, request, pk):
        serializer = DeviceTeletryHistorySerializer(data=request.query_params)
        if serializer.is_valid():
            start = serializer.data['start']
            end = serializer.data['end']
            fields = serializer.data['fields']
            queryset = Device.objects.all()
            device = get_object_or_404(queryset, pk=pk)
            data = DeviceTelemetry().query_historical_data(device.id, start, end, fields)
            return Response({
                "params": serializer.data,
                "result": data
            })
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
