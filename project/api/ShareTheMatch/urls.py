from django.conf.urls import url
from .views import user

urlpatterns = [
    url(r'users/$', user.UserCreate.as_view(), name='ShareTheMatch-create'),
]
