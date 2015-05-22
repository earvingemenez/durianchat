from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    MessageDetailAPI,
    MessageListAPI,
)

urlpatterns = (
    url(r'^$', MessageListAPI.as_view()),
    url(r'^(?P<message_id>[0-9]+)$', MessageDetailAPI.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)