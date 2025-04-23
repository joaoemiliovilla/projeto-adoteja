from django.urls import path
from . import views

urlpatterns = [
    path('adotar/<int:id>/', views.adotar_pet, name='adotar_pet'),
]