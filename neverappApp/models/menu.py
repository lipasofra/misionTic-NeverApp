from django.db import models

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    nameMenu = models.CharField('Name Menu', max_length=100)
    timeMenu = models.IntegerField(default=0)
    levelMenu = models.CharField('Level', max_length=10)