from django.db import models

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    nameIngrediente = models.CharField('Name Ingredient', max_length=100)