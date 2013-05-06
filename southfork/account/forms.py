from django import forms
from django.contrib.auth.models import User
from aapx.account.models import UserProfile, InvestorProfile, DeveloperProfile

class User_Form(forms.ModelForm):
    class Meta:
        model = User

class UserProfile_Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        
class Investor_Form(forms.ModelForm):
    class Meta:
        model = InvestorProfile

class Developer_Form(forms.ModelForm):
    class Meta:
        model = DeveloperProfile
        
class Profile_Edit_Form(forms.Form):
    email = forms.EmailField()
    primary_phone = forms.CharField(max_length=18)
    alternate_phone = forms.CharField(max_length=18, required = False)
    company_name = forms.CharField(max_length = 50, required=False)
    address_1 = forms.CharField(max_length=50)
    address_2 = forms.CharField(max_length=50, required=False)
    city = forms.CharField(max_length=40)
    postal_code = forms.CharField(max_length = 18)
    region_state = forms.CharField(max_length=40, required=False)
    country = forms.CharField(max_length=40)
    
class Authy_Form(forms.Form):
    authy_token = forms.IntegerField()
