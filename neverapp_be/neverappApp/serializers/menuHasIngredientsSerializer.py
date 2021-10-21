from rest_framework import serializers
from neverappApp.models.menuHasIngredients import MenuHasIngredient
from neverappApp.serializers.ingredientsSerializer import IngredientsSerializer
from neverappApp.serializers.menuSerializer import MenuSerializer


class MenuHasIngredientSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    ingredient = IngredientsSerializer()
    class Meta:
        model = MenuHasIngredient
        fields = ['id', 'menu', 'ingredient']