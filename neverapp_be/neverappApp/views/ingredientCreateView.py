from rest_framework import status, views
from rest_framework.response import Response
from neverappApp.serializers.ingredientsSerializer import IngredientsSerializer


class IngredientCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = IngredientsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)