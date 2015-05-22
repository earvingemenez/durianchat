from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^messages/', include('messaging.urls')),
    url(r'^accounts/', include('accounts.urls')),
]
