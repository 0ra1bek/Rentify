from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('', views.index, name='login'),
    path('register/', views.index, name='register'),
]

