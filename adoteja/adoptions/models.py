from django.db import models
from django.contrib.auth.models import User
from pets.models import Cachorro

# Create your models here.
class Adocao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adoptions')
    pet = models.ForeignKey(Cachorro, on_delete=models.CASCADE, related_name='adoptions')
    data = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'pet']
    
    def __str__(self):
        return f"{self.user.username} adotou {self.pet.nome} em {self.data.strftime('%d/%m/%Y')}"