from ShareTheMatch.serializers.meetup import MeetupSerializer
from ..models import Meetup
from rest_framework import viewsets

class MeetupViewSet(viewsets.ModelViewSet):
    queryset = Meetup.objects.all()
    serializer_class = MeetupSerializer


