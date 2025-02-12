from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Order

def add_to_order(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        
        try:
            food_name = data['food_name']
            food_price = data['food_price']
            quantity = data['quantity']
            
            order = Order(food_name=food_name, food_price=food_price, quantity=quantity)
            order.save()
            
            return JsonResponse({'status': 'success'})
        except KeyError as e:
            print(f"KeyError: {e}")
            return JsonResponse({'status': 'failed', 'message': 'Missing data'})
    else:
        return JsonResponse({'status': 'failed', 'message': 'Invalid request method'})

def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders.html', {'orders': orders})
