from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:hotel_id>/', views.food_menu, name='food_menu'),
]
