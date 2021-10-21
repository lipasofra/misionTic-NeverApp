from django.db import models

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
<<<<<<< HEAD
    nameIngrediente = models.CharField('Name Ingredient', max_length=100)
=======
    nameIngredient = models.CharField('Name Ingredient', max_length=100)
>>>>>>> 2ab57165e714fdbfa1d3e012630132cf971bf9ee
