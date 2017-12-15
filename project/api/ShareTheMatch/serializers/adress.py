from rest_framework import serializers
from ..models import Adress
from ShareTheMatch.serializers.stuff import StuffSerializer

class AdressSerializer(serializers.ModelSerializer):
    stuff = StuffSerializer(read_only=True)
    class Meta:
        model = Adress
        fields = ('city', 'country', 'user', 'post_code', 'street', 'place_id', 'created', 'stuff')