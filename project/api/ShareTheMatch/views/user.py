from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ShareTheMatch.serializers.user import UserSerializer
from django.contrib.auth.models import User

class UserCreate(APIView):

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserUpdate(APIView):
    def update(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
