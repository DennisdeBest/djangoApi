from rest_framework import serializers
from django.contrib.auth.models import User
from ..serializers import AdressSerializer


class UserSerializer(serializers.ModelSerializer):
    adresses = AdressSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'adresses')