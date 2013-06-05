# bom/urls.py
from django.conf.urls import patterns, include, url
#from bom.models import ProductInfo

urlpatterns = patterns('southfork.bom.views',
#    url(r'^(?P<product_ID>\d+)/$', 'bom_view', {'template_name':'bom/bom_view.html'}),
    url(r'productinfo/$', 'product_view', {'template_name':'bom/product_view.html'} ),
    url(r'productinfo/add_product/$', 'product_add', {'template_name':'bom/add_product.html'} ),
    url(r'productinfo/(?P<partnumber>[-\w]+)/$', 'product_detail', {'template_name':'bom/productdetail.html'} ),
#    url(r'productinfo/product_delete/(?P<product_ID>\d+)/$', 'product_delete'),
    url(r'productinfo/product_delete/(?P<part_number>\w+)/$', 'product_delete'),
    url(r'BOMInfo/$', 'bom_view', {'template_name':'bom/bom_view.html'}),
    url(r'BOMInfo/add_bom/$', 'bom_add', {'template_name':'bom/add_bom.html'} ),
    url(r'BOMinfo/(?P<bomnumber>[-\w]+)/$', 'bom_detail', {'template_name':'bom/bomdetail.html'} ),
    url(r'Components/(?P<BOM_ID>\d+)/$', 'components_view'),
    url(r'Components/add_components/$', 'components_add', {'template_name':'bom/add_components.html'}),
#    url(r'^productinfo/(?P<product_ID>\d+)/$', 'product_details', {'template_name':'bom/product_details.html'} ),
)
