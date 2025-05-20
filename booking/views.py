from django.shortcuts import render, redirect
from .models import Booking
from main.models import Property
from auth1.models import UserProfile

def booking_view(request):
    if request.method == 'POST':
        # Получаем данные из формы
        full_name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        # Получаем объект квартиры из sessionStorage
        booking_data = request.session.get('booking_data')
        if booking_data and booking_data.get('apartment'):
            property_id = booking_data['apartment']['id']
            try:
                property = Property.objects.get(id=property_id)
                
                # Создаем запись бронирования
                Booking.objects.create(
                    user=request.user if request.user.is_authenticated else None,
                    full_name=full_name,
                    phone=phone,
                    email=email,
                    property=property
                )
                
                return redirect('booking_success')
            except Property.DoesNotExist:
                pass
    
    return render(request, 'booking/booking.html')