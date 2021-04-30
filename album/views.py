from django.shortcuts import render

from .models import album
# Create your views here.

def Album(request):

    Albums= album.objects.all()

    context ={
        'album': Albums
    }
    return render(request,'album/index.html',context)