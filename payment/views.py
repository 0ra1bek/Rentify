from django.shortcuts import render

def index(request):
    return render(request ,'payment/payment.html')

def payment_success(request):
    return render(request, 'payment/success.html')