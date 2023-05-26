from django import forms
from .models import plato, Oferta

class PlatoForm(forms.ModelForm):
    class Meta:
        model = plato
        fields = ['name', 'image','restaurant', 'category', 'description', 'precio']

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['name', 'image','restaurant', 'category', 'description', 'precio', 'fecha_limite', 'precioNuevo']





