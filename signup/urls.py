from django.urls import path
from . import views

urlpatterns = [
    path("signup/",views.signup,name='signup'),
     path("home/",views.home_view,name='home_view'),
    
]