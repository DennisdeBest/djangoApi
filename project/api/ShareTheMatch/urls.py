from .views import profile, user, adress, stuff, meetup, sport, users_meetups
from rest_framework_nested import routers
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

#Hack to get fields in swagger view
class AuthTokenView(ObtainAuthToken, GenericAPIView):
    def post(self, request, *args, **kwargs):
          response = super(AuthTokenView, self).post(request, *args, **kwargs)
          token = Token.objects.get(key=response.data['token'])
          return Response({'token': token.key, 'id': token.user_id})
    pass

schema_view = get_swagger_view(title='Share The Match')

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'users', user.UserViewSet)
router.register(r'adresses', adress.AdressViewSet)
router.register(r'meetups', meetup.MeetupViewSet)
router.register(r'users-meetups', users_meetups.UsersMeetupsViewSet)

adresses_router = routers.NestedSimpleRouter(router, r'adresses', lookup='adress')
adresses_router.register(r'stuffs', stuff.StuffViewSet, base_name='adress-stuffs')

meetups_router = routers.NestedSimpleRouter(router, r'meetups', lookup='metup')
meetups_router.register(r'sports', sport.SportViewSet, base_name='metup-sports')

urlpatterns = router.urls + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [ url(r'^$', schema_view) ]
urlpatterns += [ url(r'^', include(adresses_router.urls)) ]
urlpatterns += [ url(r'^', include(meetups_router.urls)) ]
urlpatterns += [ url(r'^auth-token/', AuthTokenView.as_view())]
