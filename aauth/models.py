from django.db import models

class UserProfile(models.Model):
    # Поле для имени пользователя
    username = models.CharField(max_length=100, unique=True)
    
    # Поле для возраста
    age = models.IntegerField()

    # Поле для электронной почты
    email = models.EmailField()

    # Поле для даты регистрации
    date_joined = models.DateTimeField(auto_now_add=True)

    # Дополнительные поля
    def __str__(self):
        return self.username

