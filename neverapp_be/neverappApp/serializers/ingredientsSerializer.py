from neverappApp.models.ingredients import Ingredients
from rest_framework import serializers

class IngredientsSerializer (serializers.ModelSerializer):
    class Meta:
        model=Ingredients
        fields=['Name Ingredient']
        