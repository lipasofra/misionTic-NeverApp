from django.contrib import admin

# Register your models here.

from .models.user import User
from .models.menu import Menu

admin.site.register(User)
admin.site.register(Menu)
