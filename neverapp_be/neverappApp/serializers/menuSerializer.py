from neverappApp.models.menu import Menu
from rest_framework import serializers

class MenuSerializer (serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields=['nameMenu', 'timeMenu', 'levelMenu', 'ingredients']
        depth=1
