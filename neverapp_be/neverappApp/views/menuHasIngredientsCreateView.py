from rest_framework import status, views
from rest_framework.response import Response
from neverappApp.serializers.menuHasIngredientsSerializer import MenuHasIngredientSerializer


class MenuHasIngredientsCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = MenuHasIngredientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)