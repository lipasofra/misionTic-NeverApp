from django.db import models
from rest_framework import status, views
from rest_framework import viewsets
from rest_framework.response import Response
from neverappApp.models.ingredients import Ingredient
from neverappApp.serializers.ingredientsSerializer import IngredientsSerializer


class IngredientCreateView(viewsets.ModelViewSet):
    serializer_class = IngredientsSerializer

    '''def post(self, request, *args, **kwargs):
        serializer = IngredientsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)'''

    def get_queryset(self):
        menus = Ingredient.objects.all()
        return menus