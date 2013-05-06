from django.conf.urls import patterns
from django.contrib.auth.views import login, logout
from southfork.account.views import login_view

urlpatterns = patterns('',
                        (r'^account/login/$', login),
                        (r'^account/logout/$', logout,{'template_name':'registration/logout.html'}),
                        (r'^account/$',login_view, {'template_name':'account/account.html'}),
                        
                        )