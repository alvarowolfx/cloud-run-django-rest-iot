from rest_framework import serializers
from rest_framework.reverse import reverse
from datetime import timedelta
from django.utils import timezone

from .models import Farm, Tank, Device


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'


class DeviceListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.id


class TankSerializer(serializers.ModelSerializer):
    devices = DeviceListingField(many=True, read_only=True)

    class Meta:
        model = Tank
        fields = '__all__'


class TankListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.id


class FarmSerializer(serializers.ModelSerializer):
    tanks = TankListingField(many=True, read_only=True)

    class Meta:
        model = Farm
        fields = '__all__'


class DeviceTeletrySerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True, max_length=32)
    distance = serializers.FloatField(required=True)
    battery = serializers.FloatField(required=False)


def week():
    return timezone.now() - timedelta(days=7)


class DeviceTeletryHistorySerializer(serializers.Serializer):
    start = serializers.DateTimeField(required=False, default=week())
    end = serializers.DateTimeField(required=False, default=timezone.now())
    fields = serializers.ListField(
        required=False, default=['distance', 'battery'])
