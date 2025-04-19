<<<<<<< HEAD
from django.urls import path
from . import views

app_name = 'reg'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
=======
from django.urls import path
from . import views

app_name = 'reg' 

urlpatterns = [
    path('', views.index, name='index'),
>>>>>>> 5c41cd8 (Changes with API)
]