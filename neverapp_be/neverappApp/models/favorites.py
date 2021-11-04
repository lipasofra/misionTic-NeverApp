from django.db import models
from .user import User
from .menu import Menu

class Favorites(models.Model):
     id = models.AutoField(primary_key=True)
     user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
     menu = models.ForeignKey(Menu, related_name='menus', on_delete=models.CASCADE)


