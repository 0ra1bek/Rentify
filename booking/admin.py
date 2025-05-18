from django.contrib import admin

from django.contrib import admin
from .models import UserProfile

# Класс для настройки отображения модели UserProfile в админке
class UserProfileAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке записей
    list_display = ('username', 'email', 'age', 'date_joined')
    
    # Поля, по которым можно производить поиск
    search_fields = ('username', 'email')
    
    # Поля, по которым можно фильтровать записи
    list_filter = ('date_joined', 'age')
    
    # Поля, которые можно редактировать прямо из списка
    list_editable = ('age', 'email')
    
    # Поля, которые будут использоваться для автоматического заполнения (если нужно)
    prepopulated_fields = {}

# Регистрация модели UserProfile с настройками UserProfileAdmin
admin.site.register(UserProfile, UserProfileAdmin)