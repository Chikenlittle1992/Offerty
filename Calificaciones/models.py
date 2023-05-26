from django.db import models
from Usuarios.models import Consumidor, Restaurante
from Plato.models import plato, Oferta
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Reseña(models.Model):
    consumidor = models.ForeignKey(Consumidor, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    puntaje_calificacion = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    contenido_comentario = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.puntaje_calificacion}"

class ReseñaRestaurante(Reseña):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

class ReseñaPlato(Reseña):
    plato = models.ForeignKey(plato, on_delete=models.CASCADE)

class ReseñaOferta(Reseña):
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)

class ReseñaApp(Reseña):
    pass
