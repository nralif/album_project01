from django.urls import path,include
from . import views

app_name='blog'

urlpatterns = [
    path('',views.blueberry , name = 'blueberry')
]
