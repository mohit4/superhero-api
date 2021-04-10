from django.shortcuts import render

from rest_framework import viewsets

from .models import Weapon
from .models import Ability
from .models import Team
from .models import Costume
from .serializers import WeaponSerializer
from .serializers import AbilitySerializer
from .serializers import TeamSerializer
from .serializers import CostumeSerializer


class WeaponViewSet(viewsets.ModelViewSet):
    """Entire weapon view set with CRUD views"""
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class AbilityViewSet(viewsets.ModelViewSet):
    """Entire ability view set with CRUD views"""
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer


class TeamViewSet(viewsets.ModelViewSet):
    """Entire team view set with CRUD views"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class CostumeViewSet(viewsets.ModelViewSet):
    """Entire costume view set with CRUD views"""
    queryset = Costume.objects.all()
    serializer_class = CostumeSerializer
