from django.conf.urls import url

from rest_framework import routers

from .views import WeaponViewSet
from .views import AbilityViewSet

app_name = 'hero'

router = routers.DefaultRouter()
router.register(r'weapons', WeaponViewSet)
router.register(r'abilities', AbilityViewSet)

urlpatterns = router.urls
