from django.db import models
from food_menu.models import Food
from django.urls import reverse

class hotels(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)
    foods = models.ManyToManyField(Food, related_name='hotelss')

    def __str__(self):
        return f"{self.name}"


