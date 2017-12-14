from .views import profile, user, adress
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'users', user.UserViewSet)
router.register(r'adresses', adress.AdressViewSet)
urlpatterns = router.urls
