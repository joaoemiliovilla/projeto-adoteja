from django import forms
from .models import Cachorro

class CachorroForm(forms.ModelForm):
    class Meta:
        model = Cachorro
        fields = ['nome', 'idade', 'sexo', 'raca', 'descricao', 'imagem', 'status']