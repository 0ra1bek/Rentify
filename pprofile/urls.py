from django.urls import path
from . import views

app_name = 'pprofile'  

urlpatterns = [
    path('', views.index, name='index'),
]