from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User) #must have
    
    #phone number
    Primary_Phone = models.CharField(max_length=18, blank = True, null=True)
    Alt_Phone = models.CharField(max_length = 18, blank=True, null=True)
    
    #address
    company_name = models.CharField(max_length = 50, blank=True)
    company_reg_no = models.CharField(max_length = 30, blank=True)
    Address_1 = models.CharField(max_length = 50, blank = True)
    Address_2 = models.CharField(max_length = 50, blank = True)
    City = models.CharField(max_length = 40, blank = True)
    Postal_Code = models.CharField(max_length = 18, blank = True)
    region_state = models.CharField(max_length =40, blank = True)
    Country = models.CharField(max_length = 40, blank = True)

        