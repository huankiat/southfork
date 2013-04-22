# product/urls.py
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^bom/', include('southfork.bom.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
