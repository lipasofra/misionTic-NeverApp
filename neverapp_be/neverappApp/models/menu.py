from django.db import models
from neverappApp.models.ingredients import Ingredient

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    nameMenu = models.CharField('Name Menu', max_length=100, null=False, blank=False)
    timeMenu = models.IntegerField(default=0)
    levelMenu = models.CharField('Level', max_length=10)
    ingredients = models.ManyToManyField(Ingredient)