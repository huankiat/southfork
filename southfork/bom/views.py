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
#TODO: HK please check below code and reference line line 9 in url.py

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
def components_view(request, template_name, BOM_ID):
    components_list = get_object_or_404(Components, pk=BOM_ID)
    return render_to_response(template_name,locals(), context_instance=RequestContext(request))

@login_required(login_url='/account/login/')
def components_add(request, template_name):
    if request.method == 'POST':
        componentsform = Components_Form(request.POST, request.FILES)
        if componentsform.is_valid():
            componentsform.save()
            return HttpResponseRedirect('/bom/productinfo/')
    else:
        componentsform=Components_Form()
    return render_to_response(template_name,locals(), context_instance=RequestContext(request))



