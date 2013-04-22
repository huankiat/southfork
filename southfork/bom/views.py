# bom/views.py
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from southfork.bom.models import ProductInfo, BOMInfo, Components
from southfork.bom.forms import ProductInfo_Form, BOMInfo_Form, Components_Form

def product_view(request, template_name):
    product_list = ProductInfo.objects.all()
    return render_to_response(template_name,{'product_list': product_list})

def product_add(request, template_name):
    if request.method == 'POST':
        productinfoform = ProductInfo_Form(request.POST, request.FILES)
#        productinfoform = ProductInfo_Form(request.POST, request.FILES)
        if productinfoform.is_valid():
            productinfoform.save()
            return HttpResponseRedirect('/bom/productinfo/')
    else:
        productinfoform=ProductInfo_Form()
    return render(request, template_name, {'productinfoform': productinfoform})

def product_delete(request, product_ID):
    pd = ProductInfo.objects.get(ProductID=product_ID)
    pd.delete()
    return redirect('/bom/productinfo/')

def bom_view(request, template_name):
    bom_list = BOMInfo.objects.all()
    return render_to_response(template_name, {'bom_list': bom_list})

def bom_add(request, template_name):
    if request.method == 'POST':
        bominfoform = BOMInfo_Form(request.POST)
        if bominfoform.is_valid():
            bominfoform.save()
            return HttpResponseRedirect('/bom/BOMInfo/')
    else:
        bominfoform=BOMInfo_Form()
        return render(request, template_name, {'bominfoform':bominfoform})

def components_view(request, BOM_ID):
    components_list = get_object_or_404(Components, pk=BOM_ID)
    return render(request, 'bom/component_view.html', {'components_list': components_list})

def components_add(request, template_name):
    if request.method == 'POST':
        componentsform = Components_Form(request.POST, request.FILES)
        if componentsform.is_valid():
            componentsform.save()
            return HttpResponseRedirect('/bom/productinfo/')
    else:
        componentsform=Components_Form()
    return render(request, template_name, {'componentsform':componentsform})



