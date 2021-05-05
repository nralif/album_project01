from django.contrib import admin

from .models import post
# Register your models here.

class postAdmin(admin.ModelAdmin):

    list_display =[
        'title',
        'short_description',
        'description',
        'thumbnail'
    ]
admin.site.register(post,postAdmin)