<<<<<<< HEAD
# aauth/urls.py
from django.urls import path
from . import views

app_name = 'aauth'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

=======
from django.urls import path
from . import views

app_name = 'aauth'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]

>>>>>>> 5c41cd8 (Changes with API)
