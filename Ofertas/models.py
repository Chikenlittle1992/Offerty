from django.db import models
from Plato.models import Oferta
from Usuarios.models import Consumidor

# Create your models here.

class Favorito(models.Model):
    consumidor= models.ForeignKey(Consumidor, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.consumidor}"
