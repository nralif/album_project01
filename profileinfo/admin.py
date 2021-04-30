from django.contrib import admin

from .models import profile
# Register your models here.

class adminProfile(admin.ModelAdmin):

    list_display =[
        'name',
        'age',
        'address',
        'image'
    ]

admin.site.register(profile, adminProfile)