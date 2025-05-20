from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import UserProfile
import random

@login_required
def profile_view(request):
    try:
        user = request.user
        # Создаем профиль, если его нет (на всякий случай)
        profile, created = UserProfile.objects.get_or_create(user=user)
        
        password_form = PasswordChangeForm(user)
        
        if request.method == 'POST':
            # Обработка изменения профиля
            if 'update_profile' in request.POST:
                phone = request.POST.get('phone')
                if phone:
                    profile.phone = phone
                    profile.phone_verified = False
                    profile.save()
                    messages.success(request, "Номер телефона обновлен. Подтвердите его.")
                    return redirect('profile:profile')
            
            # Обработка подтверждения телефона
            elif 'verify_phone' in request.POST:
                if not profile.phone:
                    messages.error(request, "Сначала укажите номер телефона")
                else:
                    profile.verification_code = str(random.randint(100000, 999999))
                    profile.save()
                    messages.info(request, f"Код подтверждения отправлен на {profile.phone}")
                return redirect('profile:profile')
            
            # Обработка кода подтверждения
            elif 'confirm_code' in request.POST:
                entered_code = request.POST.get('verification_code')
                if entered_code == profile.verification_code:
                    profile.phone_verified = True
                    profile.save()
                    messages.success(request, "Телефон успешно подтвержден!")
                else:
                    messages.error(request, "Неверный код подтверждения")
                return redirect('profile:profile')
            
            # Обработка смены пароля
            elif 'change_password' in request.POST:
                form = PasswordChangeForm(user, request.POST)
                if form.is_valid():
                    user = form.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, "Пароль успешно изменен!")
                else:
                    for error in form.errors.values():
                        messages.error(request, error)
                return redirect('profile:profile')
        
        # Всегда возвращаем HttpResponse (render или redirect)
        context = {
            'user': user,
            'profile': profile,
            'password_form': password_form
        }
        return render(request, 'profile/profile.html', context)
    
    except Exception as e:
        # Логирование ошибки (в продакшене используйте logging)
        print(f"Error in profile_view: {str(e)}")
        messages.error(request, "Произошла ошибка при загрузке профиля")
        return redirect('home')  # Перенаправьте на главную или другую страницу

def index(request):
    return render(request ,'profile/profile.html')