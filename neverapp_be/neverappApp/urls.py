from django.conf.urls import url, include
from rest_framework import urlpatterns
from rest_framework import routers
from neverappApp.views.ingredientCreateView import IngredientCreateView
from neverappApp.views.menuViewSet import MenuViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("ingredient", IngredientCreateView, basename="ingredient")
router.register("menu", MenuViewSet, basename="menu")

urlpatterns = [
    url('', include(router.urls))
]
