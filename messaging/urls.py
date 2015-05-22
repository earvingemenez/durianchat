from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    # Class based views
    MessageDetailAPI,
    MessageListAPI,

    # functional views
    message_list,
    message_detail,
)

urlpatterns = (
    url(r'^$', MessageListAPI.as_view()),
    url(r'^(?P<message_id>[0-9]+)$', MessageDetailAPI.as_view()),
)


###########################################
## SAMPLE OF NON-CLASSED BASED VIEW URLS ##
###########################################
urlpatterns += (
    url(r'^fv/$', message_list),
    url(r'^fv/(?P<message_id>[0-9]+)$', message_detail),
)

# Add support format to the endpoints. [JSON, XML]
urlpatterns = format_suffix_patterns(urlpatterns)