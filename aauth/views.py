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
