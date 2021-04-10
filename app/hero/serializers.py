from rest_framework import serializers

from .models import Weapon


class WeaponSerializer(serializers.ModelSerializer):
    """Serializer for weapon"""
    class Meta:
        model = Weapon
        fields = ['name', 'description']