from django.conf.urls import url
from .views import user

urlpatterns = [
    url(r'users/$', user.UserList.as_view(), name='user-list'),
    url(r'users/$', user.UserDetail.as_view(), name='user-create'),
    url(r'users/(?P<pk>[0-9]+)/', user.UserDetail.as_view(), name='user-update'),
]
