from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from adoptions.models import Adocao

# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():  # verifica se o formulario é valido
            user = form.get_user()  # pega o usuário
            login(request, user)  # faz o login / 'login()' é uma biblioteca do django
            messages.success(request, f"Bem vindo, {user.username}")
            return redirect("home")
        else:
            messages.error(request, "Login inválido. Verifique seu usuário e senha.")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)  # sai do sistema
    messages.info(request, "Você sai da sua conta, até mais.")
    return redirect("home")  # volta para a tela de login


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  # criando formulario e preenchendo
        if form.is_valid():
            form.save()  # salva o novo usuário
            messages.success(request, "Cadastro realizado com sucesso! Faça login.")
            return redirect("login")  # envia para o login
        else:
            messages.error(request, "Erro no cadastro. Verifique os dados.")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


# função que redirecionar para a pagina de informações do usuário e passa os dados do usuário junto
@login_required  # anotação para falar que ele precisa estar logado para fazer isso
def user_profile_view(request):
    user = request.user  # pega o usuário que está logado no momento
    adocoes = Adocao.objects.filter(user=user)
    return render(request, "users/profile.html", {"user": user, "adocoes": adocoes})
