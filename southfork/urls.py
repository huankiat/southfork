# product/urls.py
from django.conf.urls import patterns, include, url
from django.contrib import admin
from southfork.views import home_view
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home_view, {'template_name':'index.html'}),
    url(r'^bom/', include('southfork.bom.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
