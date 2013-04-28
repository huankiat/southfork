from southfork.bom.models import ProductInfo, BOMInfo, Components
from django.contrib import admin

admin.site.register(ProductInfo)
admin.site.register(BOMInfo)
admin.site.register(Components)


#TODO change formating in admin page, include classes, field, imort only specific models
# use templates