from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Meal(models.Model):
    meal_type = models.CharField(max_length=64)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FoodItem(models.Model):
    name = models.CharField(max_length=256)
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()


class MealEntry(models.Model):
    quantity = models.FloatField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
