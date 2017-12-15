from ShareTheMatch.serializers.stuff import StuffSerializer
from ..models import Stuff
from rest_framework import viewsets
# from rest_framework.decorators import detail_route


class StuffViewSet(viewsets.ModelViewSet):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer

