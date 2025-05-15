from django.shortcuts import render

def index(request):
    return render(request, 'pprofile/index.html')

def profile_view(request):
    return render(request, 'pprofile/profile.html') 
