from django.contrib import admin
#from .models import User
from django.contrib.auth.admin import UserAdmin

from pythonfi_web.admin_fi.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_confirmed')

admin.site.register(Profile, ProfileAdmin)