from django.conf.urls import url

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from .views import WeaponViewSet
from .views import AbilityViewSet

app_name = 'hero'

router = routers.DefaultRouter()
router.register(r'weapons', WeaponViewSet)
router.register(r'abilities', AbilityViewSet)

schema_view = get_swagger_view(title='SuperHero API')

urlpatterns = [
    url('docs/', schema_view),
] + router.urls
