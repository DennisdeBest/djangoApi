from .views import user
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash = False)

router.register(r'users', user.UserViewSet)
urlpatterns = router.urls
