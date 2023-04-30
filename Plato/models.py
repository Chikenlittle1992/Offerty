from django.db import models
from Usuarios import models as modelosUsuarios

class plato(models.Model):
    id = models.BigAutoField(primary_key=True)
    name= models.CharField(max_length= 50, default='')
    restaurant = models.ForeignKey(modelosUsuarios.Restaurante,to_field='Nombre_Marca', null= False, blank=False, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, default='', null= False, blank=False)
    description = models.CharField(max_length = 250, default='')
    #images = models.ImageField(upload_to="media/services/images", null=True)
# Create your models here.
