from django.db import models

class FoodRequest(models.Model):
    user_name = models.CharField(max_length=100)
    food_details = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
