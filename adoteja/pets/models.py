from django.db import models

# Create your models here.

class Cachorro(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(
        max_length=20,
        choices=[('Macho', 'Macho'), ('Fêmea', 'Fêmea')]
    )
    raca = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='cachorros/')
    status = models.CharField(
        max_length=20,
        choices=[('Disponível', 'Disponível'), ('Adotado', 'Adotado'), ('Em processo','Em processo')],
        default='Disponível'
    )
    
    def __str__(self):
        return self.nome