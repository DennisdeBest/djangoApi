from rest_framework import serializers
from django.contrib.auth.models import User
from ..serializers import AdressSerializer, MeetupSerializer
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    adresses = AdressSerializer(many=True, read_only=True)
    meetups = MeetupSerializer(many=True, read_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=100)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'adresses', 'meetups')

    def create(self, validated_data):

        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            last_name=validated_data['last_name'],
            first_name=validated_data['first_name'],
        )
        user.save()
        return user
