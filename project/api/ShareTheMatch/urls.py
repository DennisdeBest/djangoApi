from .views import profile, user, adress, stuff
from rest_framework_nested import routers
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Share The Match')

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'users', user.UserViewSet)
router.register(r'adresses', adress.AdressViewSet)


adresses_router = routers.NestedSimpleRouter(router, r'adresses', lookup='adress')
adresses_router.register(r'stuffs', stuff.StuffViewSet, base_name='adress-stuffs')

# router.register(r'stuffs', stuff.StuffViewSet)

urlpatterns = router.urls + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [ url(r'^$', schema_view) ]
urlpatterns += [ url(r'^', include(adresses_router.urls)) ]
