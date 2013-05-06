from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext


@login_required(login_url='/account/login/')
def login_view(request,template_name):
    request.session['name'] = request.user.id
    session = request.session
    user = request.user
    try:
        profile = request.user.get_profile()
    except:
        pass
    return render_to_response(template_name,locals(), context_instance=RequestContext(request))

