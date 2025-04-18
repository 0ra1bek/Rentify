from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 
    path('main1/', include('main1.urls')),
    path('auth/', include('aauth.urls')),
    path('reg/', include('reg.urls')),  
    path('booking/', include('booking.urls')),
    path('payment/', include('payment.urls')),
    path('pprofile/', include('pprofile.urls')),
    path('pass/', include('pass.urls')),
    path('like/', include('like.urls')),
]

