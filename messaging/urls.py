from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    MessageDetailAPI,
    CreateMessageAPI,
)

urlpatterns = (
    url(r'^(?P<message_id>[0-9]+)$', MessageDetailAPI.as_view()),
    url(r'^create$', CreateMessageAPI.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)