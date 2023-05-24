from django.db import models
from Usuarios import models as modelosUsuarios

class plato(models.Model):
    id = models.BigAutoField(primary_key=True)
    name= models.CharField(max_length= 50, default='')
    image = models.ImageField(verbose_name='Imagen', null=True)
    restaurant = models.ForeignKey(modelosUsuarios.Restaurante,to_field='Nombre_Marca', null= False, blank=False, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, default='', null= False, blank=False)
    description = models.CharField(max_length = 250, default='')
    precio = models.IntegerField(default=0)

    def es_oferta(self):
        return False
    def __str__(self):
        return self.name

class Oferta(plato):
    fecha_limite = models.DateField()
    precioNuevo = models.IntegerField(default=0)
    def es_oferta(self):
        return True
