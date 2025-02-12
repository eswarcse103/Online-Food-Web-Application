from django.contrib import admin

from .models import Food

class FoodsAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'food_image', 'food_price')

admin.site.register(Food,FoodsAdmin)    