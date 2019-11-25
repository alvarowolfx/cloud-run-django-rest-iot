from rest_framework import serializers
from rest_framework.reverse import reverse

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
