from ShareTheMatch.serializers.user import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
# from rest_framework.decorators import detail_route


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


