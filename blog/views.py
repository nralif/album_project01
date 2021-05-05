from django.shortcuts import render

from .models import post
# Create your views here.
def blogList(request):
    
    posts= post.objects.all()

    context={
        'Posts':posts
    }
    return render(request, 'blog/index.html',context)
