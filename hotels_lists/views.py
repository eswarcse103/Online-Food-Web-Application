from django.shortcuts import render
from .models import hotels


def hotel_list(request):
    hotel = hotels.objects.all()
    return render(request, 'hotels_lists/hotels_lists.html', {'Hotel': hotel})

