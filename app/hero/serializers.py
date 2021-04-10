from rest_framework import serializers

from .models import Weapon
from .models import Ability
from .models import Team
from .models import Costume
from .models import Hero


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


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for super hero team"""
    class Meta:
        model = Team
        fields = ['name', 'motive', 'location']


class CostumeSerializer(serializers.ModelSerializer):
    """Serializer for super hero costume"""
    class Meta:
        model = Costume
        fields = ['top', 'top_color', 'bottom', 'bottom_color', 'cape', 'cape_color', 'mask', 'mask_color']


class HeroSerializer(serializers.ModelSerializer):
    """Serializer for hero"""
    class Meta:
        model = Hero
        fields = ['name', 'created', 'modified', 'real_name', 'aliases', 'costume', 'weapons', 'abilities', 'affiliations']
