"""neverappProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.urls.conf import include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from neverappApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    #prueba
    path('favorites/create/', views.FavoritesCreateView.as_view()),
    path('favorites/<int:user>/<int:pk>/', views.FavoritesDetailView.as_view()),
    path('favorites/update/<int:user>/<int:pk>/', views.FavoritesUpdateView.as_view()),
    path('favorites/remove/<int:user>/<int:pk>/', views.FavoritesDeleteView.as_view()),
    path('favorites list/<int:user>/', views.FavoritesUserView.as_view()),
    #path('userCreateFavorites/', views.UserFavoritesCreateView.as_view()),
    #path('userDetailFavorites/<int:pk>/', views.UserFavoritesDetailView.as_view()),
    path('neverappApp/', include('neverappApp.urls'))
]
