from ShareTheMatch.serializers.adress import AdressSerializer
from ..models import Adress
from rest_framework import viewsets
# from rest_framework.decorators import detail_route


class AdressViewSet(viewsets.ModelViewSet):
    queryset = Adress.objects.all()
    serializer_class = AdressSerializer

    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_staff:
            return Adress.objects.all()
        return Adress.objects.filter(user=user)


