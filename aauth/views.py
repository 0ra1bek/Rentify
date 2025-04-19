<<<<<<< HEAD
# aauth/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main1:index')
        else:
            messages.error(request, "Неверные учетные данные")
    else:
        form = AuthenticationForm()
    return render(request, 'aauth/auth.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main:index')

def index(request):
    return redirect('aauth:login')
=======
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:index')
        else:
            messages.error(request, "Неверные учетные данные")
    else:
        form = AuthenticationForm()
    return render(request, 'aauth/auth.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = UserCreationForm()
    return render(request, 'reg/reg.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main:index')
>>>>>>> 5c41cd8 (Changes with API)
