from ShareTheMatch.serializers.users_meetups import UsersMeetupsSerializer
from ..models import UsersMeetups
from rest_framework import viewsets


class UsersMeetupsViewSet(viewsets.ModelViewSet):
    queryset = UsersMeetups.objects.all()
    serializer_class = UsersMeetupsSerializer

