from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pets.models import Cachorro
from .models import Adocao

# Create your views here.


@login_required  # só funciona se tiver logado
def adotar_pet(request, id):
    pet = get_object_or_404(Cachorro, id=id)  # pega o cachorro pelo id
    user = request.user  # pega o usuario que está logado

    # verificar se o cachorro ja foi adotado
    if Adocao.objects.filter(user=user, pet=pet).exists():
        messages.info(request, f"Você já adotou o {pet.nome}")
    else:
        Adocao.objects.create(user=user, pet=pet) # criando a adocao do cachorro
        messages.success(request, f"{pet.nome} foi adicionado á sua lista de adoções!")
    
    return redirect('detalhes_cachorro', id=pet.id)