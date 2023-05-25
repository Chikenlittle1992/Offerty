from django import forms
from Calificaciones.models import ReseñaApp, ReseñaRestaurante, ReseñaPlato, ReseñaOferta

class CreacionNuevaReseñaPlato(forms.ModelForm):

    class Meta:
        model = ReseñaPlato
        fields = ("puntaje_calificacion", "contenido_comentario")

class CreacionNuevaReseñaOferta(forms.ModelForm):

    class Meta:
        model = ReseñaOferta
        fields = ("puntaje_calificacion", "contenido_comentario")

class CreacionNuevaReseñaRestaurante(forms.ModelForm):

    class Meta:
        model = ReseñaRestaurante
        fields = ("puntaje_calificacion", "contenido_comentario")

class CreacionNuevaReseñaApp(forms.ModelForm):

    class Meta:
        model = ReseñaApp
        fields = ("puntaje_calificacion", "contenido_comentario")