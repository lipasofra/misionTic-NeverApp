from django.db.models import query
from rest_framework import status, views
from rest_framework import viewsets
from rest_framework.response import Response
from neverappApp.models.ingredients import Ingredient
from neverappApp.models.menu import Menu
from neverappApp.serializers.menuSerializer import MenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer

    def get_queryset(self):
        querySet = Menu.objects.all()
        ingredient = self.request.query_params.get('ingredient', None)
        if ingredient is not None:
            querySet = querySet.filter(ingredients=ingredient)

        return querySet

    def create(self, request, *args, **kwargs):
        data = request.data
        new_menu = Menu.objects.create(nameMenu=data["nameMenu"], timeMenu=data['timeMenu'], levelMenu=data['levelMenu'])
        new_menu.save()

        for ingredient in data['ingredients']:
            ingredient_obj = Ingredient.objects.get(nameIngredient=ingredient['nameIngredient'])
            new_menu.ingredients.add(ingredient_obj)

        serializer = MenuSerializer(new_menu)

        return Response(serializer.data)