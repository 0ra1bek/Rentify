from django.urls import path
from . import views

app_name = 'reg'

urlpatterns = [
    path('', views.index, name='index'),
    path('reg/', views.register_view, name='register'),
]