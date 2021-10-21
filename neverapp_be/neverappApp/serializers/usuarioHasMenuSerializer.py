from rest_framework import serializers
from neverappApp.serializers.userSerializer import UserSerializer
from neverappApp.serializers.menuSerializer import MenuSerializer
from neverappApp.models.UsuarioHasMenu import UsuarioHasMenu


class UsuarioHasMenuSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    user= UserSerializer()
    class Meta:
        model = UsuarioHasMenu
        fields = ['id', 'user', 'menu']