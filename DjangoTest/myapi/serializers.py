from rest_framework import serializers

from myapi.models import Hero, Monster

class HeroSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    hitpoints = serializers.IntegerField()
    strength = serializers.IntegerField()
    mana = serializers.IntegerField()
    gold = serializers.DecimalField(decimal_places=4, max_digits=20)
    email = serializers.EmailField()

class MonsterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    hitpoints = serializers.IntegerField()