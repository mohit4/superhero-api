from django.shortcuts import render

from rest_framework import viewsets

from .models import Weapon
from .models import Ability
from .serializers import WeaponSerializer
from .serializers import AbilitySerializer


class WeaponViewSet(viewsets.ModelViewSet):
    """Entire weapon view set with CRUD views"""
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class AbilityViewSet(viewsets.ModelViewSet):
    """Entire ability view set with CRUD views"""
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer
