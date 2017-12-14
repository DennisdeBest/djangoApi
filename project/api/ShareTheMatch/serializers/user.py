from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    adresses = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'adresses')