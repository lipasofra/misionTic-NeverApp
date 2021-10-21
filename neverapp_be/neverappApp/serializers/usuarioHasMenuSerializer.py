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

    '''def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        UsuarioHasMenu = UsuarioHasMenu.objects.get(id=obj.id)
        user = User.objects.get(user=obj.id)
        menu = Menu.objects.get(menu=obj.id)
        return {
            'id': UsuarioHasMenu.id,
            'user': user.username,
            'menu': menu.nameMenu,
        }'''