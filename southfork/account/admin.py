from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from southfork.account.models import UserProfile

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline,]
    
#TODO: get everything inline in admin view
admin.site.register(User, UserProfileAdmin)


