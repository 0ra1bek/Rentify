from django.urls import path
from . import views

app_name = 'face'  

urlpatterns = [
    path('', views.index, name='index'),
]