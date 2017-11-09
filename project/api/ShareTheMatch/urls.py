from django.conf.urls import url
from .views import user

urlpatterns = [
    url(r'users/$', user.STMUser.as_view(), name='ShareTheMatch-create'),
    url(r'users/(?P<pk>\d+)/',user.STMUser.as_view(), name='ShareTheMatch-delete'),
]
