from ShareTheMatch.serializers.sport import SportSerializer
from ..models import Sport
from rest_framework import viewsets

class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


