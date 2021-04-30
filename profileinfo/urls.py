from django.urls import path, include

from . import views

app_name = 'profileinfo'

urlpatterns = [
    path('',views.homepage, name='homepage')
]

