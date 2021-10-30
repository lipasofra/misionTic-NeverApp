from rest_framework import serializers
from neverappApp.models.user import User
from neverappApp.models.menu import Menu
from neverappApp.models.favorites import Favorites


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['id', 'user_Name', 'name_Menu']

    def to_representation(self, obj):
        favorites = Favorites.objects.get(id=obj.id)
        user = User.objects.get(id=favorites.user_Name_id)
        menu = Menu.objects.get(id=favorites.name_Menu_id)

        return {
            'id': favorites.id,
            'user_Name': favorites.name,
            'name_Menu': favorites.name_Menu,
            }
