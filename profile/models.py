from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.utils import timezone

class UserProfile(models.Model):
    """
    Расширенная модель профиля пользователя с:
    - Верификацией телефона
    - Настройками уведомлений
    - Дополнительными метаданными
    """
    # Связь с пользователем
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='userprofile',
        verbose_name='Пользователь'
    )
    
    # Валидатор для номера телефона
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Номер телефона должен быть в формате: '+999999999'"
    )
    
    # Основные поля
    phone = models.CharField(
        'Телефон',
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
        unique=True
    )
    phone_verified = models.BooleanField(
        'Телефон подтвержден',
        default=False
    )
    verification_code = models.CharField(
        'Код подтверждения',
        max_length=6,
        blank=True,
        null=True
    )
    verification_code_sent_at = models.DateTimeField(
        'Код отправлен',
        blank=True,
        null=True
    )
    
    # Настройки уведомлений
    email_notifications = models.BooleanField(
        'Email уведомления',
        default=True
    )
    sms_notifications = models.BooleanField(
        'SMS уведомления',
        default=True
    )
    push_notifications = models.BooleanField(
        'Push уведомления',
        default=True
    )
    
    # Метаданные
    created_at = models.DateTimeField(
        'Создан',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Обновлен',
        auto_now=True
    )
    
    # Аватар пользователя
    avatar = models.ImageField(
        'Аватар',
        upload_to='avatars/',
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Профиль {self.user.username}'
    
    def generate_verification_code(self):
        """Генерация 6-значного кода подтверждения"""
        import random
        self.verification_code = str(random.randint(100000, 999999))
        self.verification_code_sent_at = timezone.now()
        self.save()
        return self.verification_code
    
    def verify_phone(self, code):
        """Проверка кода подтверждения"""
        if self.verification_code == code:
            self.phone_verified = True
            self.save()
            return True
        return False

# Сигналы для автоматического создания профиля
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()