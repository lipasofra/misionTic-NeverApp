from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from neverappApp.serializers.userSerializer import UserSerializer
from neverappApp.models.menu import Menu
from neverappApp.models.user import User
from rest_framework.permissions import IsAuthenticated

from django.conf import settings
from rest_framework_simplejwt.backends import TokenBackend

class UserFavoritesCreateView(views.APIView):
    #permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)


        data = request.data
        usuario = User.objects.get(id=data["id_user"])
        new_favorite = Menu.objects.get(nameMenu=data["nameMenu"])
        usuario.favorite_menus.add(new_favorite)

        serializer = UserSerializer(usuario)

        return Response(serializer.data)