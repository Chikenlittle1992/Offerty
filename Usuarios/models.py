from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=254,unique = True)
    is_consumidor = models.BooleanField(default=False)
    is_restaurante = models.BooleanField(default=False)

    @property
    def is_Consumidor(self):
        return self.is_consumidor
    
    @property
    def is_Restaurante(self):
        return self.is_restaurante

class Consumidor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='Consumidor')
    Nombre = models.CharField(max_length=100)

class Restaurante(models.Model):
    Nombre_Marca = models.CharField(max_length=100,unique=True)
    ubicacion = models.CharField(max_length=100)