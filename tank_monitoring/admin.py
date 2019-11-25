from django.contrib import admin
from .models import Farm, Tank, Device


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
    search_fields = ('name', 'description')


@admin.register(Tank)
class TankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'farm', 'latitude',
                    'longitude', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('farm',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('deviceId', 'tank', 'created_at')
    search_fields = ('deviceId',)
    list_filter = ('tank',)
