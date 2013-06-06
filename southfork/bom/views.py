# bom/views.py
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from southfork.bom.models import ProductInfo, BOMInfo, Components
from southfork.bom.forms import ProductInfo_Form, BOMInfo_Form, Components_Form

@login_required(login_url='/account/login/')
def product_view(request, template_name):
    product_list = ProductInfo.objects.all()
    return render_to_response(template_name,locals(), context_instance=RequestContext(request))

@login_required(login_url='/account/login/')
def product_add(request, template_name):
    if request.method == 'POST':
        productinfoform = ProductInfo_Form(request.POST, request.FILES)
        if productinfoform.is_valid():
            productinfoform.save()
            return HttpResponseRedirect('/bom/productinfo/')
    else:
        productinfoform=ProductInfo_Form()
    return render_to_response(template_name,locals(), context_instance=RequestContext(request))

@login_required(login_url='/account/login/')
def product_detail(request, template_name, partnumber):
    productdetail = ProductInfo.objects.all()
    pd=ProductInfo.objects.get(part_number=partnumber)
    return render_to_response(template_name,locals(), context_instance=RequestContext(request))

@login_required(login_url='/account/login/')
def product_delete(request, part_number):
    pd = ProductInfo.objects.get(part_number=part_number)
    pd.delete()
    return redirect('/bom/productinfo/')

@login_required(login_url='/account/login/')
def bom_view(request, template_name):
    bom_list = BOMInfo.objects.all()
    return render_to_response(template_name,locals(), context_instance=RequestContext(request))

#TODO: Huankiat - please review rows 44-47 here and bomdetail.html file...qty is not showing up in bomdetail.html
@login_required(login_url='/account/login/')
def bom_detail(request, template_name, bomnumber):
    bomdetail = BOMInfo.objects.all()
    bdbn=BOMInfo.objects.get(bom_number=bomnumber)
    return render_to_response(template_name,locals(), context_instance=RequestContext(request))

#TODO: Xuan how to add multiple rows of data in one page? See add_bom.html and http://127.0.0.1:8000/bom/Components/add_components/
@login_required(login_url='/account/login/')
def bom_add(request, template_name):
    if request.method == 'POST':
        bominfoform = BOMInfo_Form(request.POST)
        if bominfoform.is_valid():
            bominfoform.save()
            return HttpResponseRedirect('/bom/BOMInfo/')
    else:
        bominfoform=BOMInfo_Form()
    return render_to_response(template_name,locals(), context_instance=RequestContext(request))

@login_required(login_url='/account/login/')
def components_view(request, template_name):
    components_list = Components.objects.all()
#    cd = Components.objects.get(part_number=partnumber)
    return render_to_response(template_name,locals(), context_instance=RequestContext(request))

#@login_required(login_url='/account/login/')
#def components_detail(request, template_name, compbomnumber):
#    compdetail = Components.objects.all()
#    cd=Components.objects.get(bom=compbomnumber)
#    return render_to_response(template_name,locals(), context_instance=RequestContext(request))

@login_required(login_url='/account/login/')
def components_add(request, template_name):
    if request.method == 'POST':
        componentsform = Components_Form(request.POST, request.FILES)
        if componentsform.is_valid():
            componentsform.save()
            return HttpResponseRedirect('/bom/BOMInfo/')
    else:
        componentsform=Components_Form()
    return render_to_response(template_name,locals(), context_instance=RequestContext(request))



