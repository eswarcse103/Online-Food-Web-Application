from django.urls import path
from . import views


urlpatterns = [
     path('add_to_order/', views.add_to_order, name='add_to_order'),
    path('', views.orders_list,name="orders_list"),
]
