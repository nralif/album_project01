from django.contrib import admin

from .models import album
# Register your models here.

class albumAdmin(admin.ModelAdmin):

    list_display = [
        'description',
        'creation',
        'thumbnail',

    ]
admin.site.register(album, albumAdmin)