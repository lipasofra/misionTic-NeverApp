from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from neverappApp.models.user import User
from neverappApp.serializers.userSerializer import UserSerializer

class UserFavoritesDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        id_usuario = self.request.query_params.get('id_user', None)
        usuario = User.objects.get(id=id_usuario)

        print(usuario)
        return Response(usuario.favorite_menus.all())

"""
        data = request.data
        print('#############################################',data)
        id_usuario = data['user_id']
        print(id_usuario)
        usuario = self.queryset.filter(id=id_usuario)
        print(usuario)
        favoritos = usuario.favorite_menus
        print(favoritos)

        #return super().get(request, *args, **kwargs)
        return favoritos"""