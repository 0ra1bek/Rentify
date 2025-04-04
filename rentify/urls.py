from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aauth.urls')),
    path('login/', include('aauth.urls')),
    path('main/', include('main.urls')),
    path('reg/', include('reg.urls')),
]

