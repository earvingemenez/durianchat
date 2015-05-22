from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import ObtainAuthToken

from .views import UserAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = patterns('',

    url(r'^$', UserListAPIView.as_view()),
    url(r'^me$', UserAPIView.as_view(), name='user_view'),
    url(r'^(?P<user_id>[0-9]+)$', UserDetailAPIView.as_view()),
    url(r'^authenticate$', ObtainAuthToken.as_view()),
)