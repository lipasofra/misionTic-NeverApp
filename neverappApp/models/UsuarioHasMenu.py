from django.db import models
from .user import User
from .menu import Menu

class UsuarioHasMenu(models.Model):
    user = models.ForeignKey(User, related_name='UsuarioHasMenu', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, related_name='UsuarioHasMenu', on_delete=models.CASCADE)