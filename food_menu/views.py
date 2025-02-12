from django.shortcuts import render, get_object_or_404
from hotels_lists.models import hotels

def food_menu(request, hotel_id):
    hotel = get_object_or_404(hotels, id=hotel_id)
    foods = hotel.foods.all()
    return render(request, 'food_menu/food_menu.html', {'hotel': hotel, 'foods': foods})
