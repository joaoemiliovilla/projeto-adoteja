from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home_pets'),
    path('adicionar/', views.adicionar_cachorro, name='adicionar_cachorro'),
]