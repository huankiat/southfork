# product/urls.py
from django.conf.urls import patterns, include, url
from django.contrib import admin
from southfork.views import home_view
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home_view, {'template_name':'index.html'}),
    url(r'', include('southfork.account.urls')),
    url(r'^bom/', include('southfork.bom.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


# serving static and media files while in production
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^public_media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)