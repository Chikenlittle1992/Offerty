from django.contrib import admin
from Calificaciones.models import Reseña, ReseñaApp, ReseñaPlato, ReseñaRestaurante, ReseñaOferta

# Register your models here.

admin.site.register(Reseña)
admin.site.register(ReseñaApp)
admin.site.register(ReseñaPlato)
admin.site.register(ReseñaOferta)
admin.site.register(ReseñaRestaurante)