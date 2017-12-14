from .views import profile
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash = False)

router.register(r'users', profile.ProfileViewSet)
urlpatterns = router.urls
