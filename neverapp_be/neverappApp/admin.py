from django.contrib import admin

# Register your models here.

from .models.user import User
from .models.menu import Menu
from .models.favorites import Favorites
from .models.ingredients import Ingredient

admin.site.register(User)
admin.site.register(Menu)
