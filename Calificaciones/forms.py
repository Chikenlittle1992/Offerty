from django import forms
from Calificaciones.models import ReseñaApp, ReseñaRestaurante, ReseñaPlato

class CreacionNuevaReseñaPlato(forms.ModelForm):
    consumidor = forms.CharField(widget=forms.HiddenInput())
    plato = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = ReseñaPlato
        fields = ("consumidor", "puntaje_calificacion", "contenido_comentario", "plato")