
from django.db import models


class Farm(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tank(models.Model):
    farm = models.ForeignKey(Farm, related_name='tanks',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.CharField(blank=True, max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    tank = models.ForeignKey(Tank, related_name='devices',
                             null=True, on_delete=models.SET_NULL)
    deviceId = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.deviceId
