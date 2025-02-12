from django.db import models

class Order(models.Model):
    food_name = models.CharField(max_length=100)
    food_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.food_name} - {self.quantity}"
