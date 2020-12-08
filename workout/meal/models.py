from django.db import models

# Create your models here.
class Meal(models.Model):
    """食品データベース"""
    food = models.CharField(max_length=100,null=False)
    energy = models.FloatField(null=False)
    protein = models.FloatField(null=False)
    fat = models.FloatField(null=False)
    carbo = models.FloatField(null=False)
