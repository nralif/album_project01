from django.shortcuts import render

# Create your views here.
def blueberry(request):

    context={

    }
    return render(request, 'blog/index.html',context)
