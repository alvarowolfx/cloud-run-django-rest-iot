from rest_framework import routers

from .views import FarmViewSet, TankViewSet, DeviceViewSet

router = routers.DefaultRouter()
router.register('farms', FarmViewSet)
router.register('tanks', TankViewSet)
router.register('devices', DeviceViewSet)

urlpatterns = router.urls
