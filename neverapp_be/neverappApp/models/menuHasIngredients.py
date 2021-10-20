from django.db import models
from .ingredients import Ingredient
from .menu import Menu

class MenuMenu(models.Model):
    menu = models.ForeignKey(Menu, related_name='menus', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, related_name='ingredients', on_delete=models.CASCADE)