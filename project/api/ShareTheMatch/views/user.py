from ShareTheMatch.serializers.user import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import permission_classes

from rest_framework.permissions import AllowAny
from ..custom_permissions import AllowPostAny

# @permission_classes((AllowPostAny, ))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.all()

