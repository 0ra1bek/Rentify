from django.shortcuts import render
from .models import Property

def index(request):
    rooms_filter = request.GET.get('rooms')
    properties = Property.objects.all()
    if rooms_filter:
        properties = properties.filter(rooms=rooms_filter)
    return render(request, 'main1/main1.html', {'properties': properties})