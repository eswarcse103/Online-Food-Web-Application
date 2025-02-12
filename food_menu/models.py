from django.db import models

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=50)
    food_price = models.DecimalField(max_digits=6, decimal_places=2)
    food_image = models.ImageField(upload_to="Food_image/", blank=True,null=True)

    def __str__(self):
        return f"{self.food_name}"

