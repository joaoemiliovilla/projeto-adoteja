from django.shortcuts import render, redirect

# Create your views here.

from .models import Cachorro
from .forms import CachorroForm

def home(request):
    # cachorros_disponiveis = Cachorro.objects.filter(status='Disponível')
    cachorros = Cachorro.objects.all()
    return render(request, 'home.html', { 'cachorros': cachorros })

def adicionar_cachorro(request):
    if request.method == "POST":
        form = CachorroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CachorroForm()
    return render(request, 'adicionar_cachorro.html', {'form': form})
