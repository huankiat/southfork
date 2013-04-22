# bom/views.py
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext

def normal_processor(request):
    key_info = {'key_contact':'Dilan Seneviratne',
                'email_contact':'dilans@alum.mit.edu',
                'copyright_info':'Copywrite 2013 by VF Nexus',
                }
    
    return key_info

def home_view(request, template_name):
    return render(request, template_name,{'site_name': 'SouthFork Project - BOM Prototype'},\
                  context_instance=RequestContext(request, processors=[normal_processor]))

