from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ShareTheMatch.serializers.user import UserSerializer
from django.contrib.auth.models import User


class STMUser(APIView):

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        user = request.user
        if not user.is_authenticated:
            return Response(status=status.HTTP_403_FORBIDDEN)
        from rest_framework.generics import get_object_or_404
        user = get_object_or_404(User, pk=pk, user=user)
        user.delete()
        return Response(status=status.HTTP_200_OK)