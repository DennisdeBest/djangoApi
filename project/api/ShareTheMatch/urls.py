from .views import profile, user, adress
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Share The Match')

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'users', user.UserViewSet)
router.register(r'adresses', adress.AdressViewSet)
urlpatterns = router.urls + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    url(r'^$', schema_view)
    ]

