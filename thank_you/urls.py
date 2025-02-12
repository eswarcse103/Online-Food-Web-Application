from django.urls import path
from . import views


urlpatterns = [
    path('',views.thank_you, name='thank_you'),
]