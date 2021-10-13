from django.contrib import admin

# Register your models here.

from .models.user import User
from .models.menu import Menu
from .models.UsuarioHasMenu import UsuarioHasMenu

admin.site.register(User)
admin.site.register(Menu)
admin.site.register(UsuarioHasMenu)
