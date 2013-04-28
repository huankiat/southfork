from django import forms
from southfork.bom.models import ProductInfo, BOMInfo, Components

class ProductInfo_Form(forms.ModelForm):
	class Meta:
		model=ProductInfo
		exclude=('created_at', 'updated_at', 'bom_number',)

class BOMInfo_Form(forms.ModelForm):
	class Meta:
		model=BOMInfo

class Components_Form(forms.ModelForm):
	class Meta:
		model=Components

#class Product_BOM_History_Form(forms.ModelForm):
#    class Meta:
#        model=Product_BOM_History
#
#class BOMID_ComponentID_Form(forms.ModelForm):
#    class Meta:
#        model=BOMID_ComponentID

#class Product_Route_Form(forms.ModelForm):
#    class Meta:
#        model=Product_Route

#class Route_Form(forms.ModelForm):
#    class Meta:
#        model=Route

#class Operation_Recipe_Equipment_Form(forms.ModelForm):
#    class Meta:
#        model=Operation_Recipe_Equipment

#class EquipmentGroup_Equipment_Form(forms.ModelForm):
#    class Meta:
#        model=EquipmentGroup_Equipment

#class Equipment_Form(forms.ModelForm):
#    class Meta:
#        model=Equipment

#class Recipe_Form(forms.ModelForm):
#    class Meta:
#        model=Recipe