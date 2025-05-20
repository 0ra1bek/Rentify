from django.contrib import admin
from .models import Booking  # Импортируем только модель Booking

admin.site.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'property')
    search_fields = ('full_name', 'phone', 'email', 'property__title')
    date_hierarchy = 'created_at'