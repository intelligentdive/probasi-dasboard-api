from django.contrib import admin

from . import models
from .models import Profileinfo1, Profileinfolocationbd, Profileinfolocationabroad, Profileinfoexperience

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")


admin.site.register(models.User, UserAdmin)



@admin.register(Profileinfo1)
class Profileinfo1Admin(admin.ModelAdmin):
    list_display = ('user', 'user_name', 'gender', 'date_of_birth')

@admin.register(Profileinfolocationbd)
class ProfileinfolocationbdAdmin(admin.ModelAdmin):
    list_display = ('user', 'District')

@admin.register(Profileinfolocationabroad)
class ProfileinfolocationabroadAdmin(admin.ModelAdmin):
    list_display = ('user', 'countryname', 'city', 'duration')

@admin.register(Profileinfoexperience)
class ProfileinfoexperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'industry', 'areaofexpertise', 'durationstay')
