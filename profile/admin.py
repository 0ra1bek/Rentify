from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'phone_verified', 'created_at')
    list_filter = ('phone_verified', 'created_at')
    search_fields = ('user__username', 'phone')
    readonly_fields = ('created_at', 'updated_at')