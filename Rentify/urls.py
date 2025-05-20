from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('face.urls')), 
    path('main/', include('main.urls')),
    path('auth/', include('auth1.urls')),
    path('reg/', include('reg.urls')),  
    path('booking/', include('booking.urls')),
    path('payment/', include('payment.urls')),
    path('profile/', include('profile.urls')),
    path('pass/', include('pass.urls')),
    path('favorites/', include('favorites.urls')),
]

