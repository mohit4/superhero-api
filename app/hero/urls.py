from django.conf.urls import url

from rest_framework import routers

from .views import WeaponViewSet

app_name = 'hero'

router = routers.DefaultRouter()
router.register(r'weapons', WeaponViewSet)

urlpatterns = router.urls
