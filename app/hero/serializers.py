from rest_framework import serializers

from .models import Weapon
from .models import Ability


class WeaponSerializer(serializers.ModelSerializer):
    """Serializer for weapon"""
    class Meta:
        model = Weapon
        fields = ['name', 'description']


class AbilitySerializer(serializers.ModelSerializer):
    """Serializer for super hero ability"""
    class Meta:
        model = Ability
        fields = ['ability', 'description', 'origin']
