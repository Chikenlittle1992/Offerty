from django.shortcuts import render, get_object_or_404
from .models import plato, Oferta
from Calificaciones.models import ReseñaOferta, ReseñaPlato
from Calificaciones.views import crearNuevaReseñaPlato

# Create your views here.

def platoDetalles(request, plato_id):
    reseñasPlato = ''
    platoDetalle = get_object_or_404(plato, pk=plato_id)
    existe = Oferta.objects.filter(pk=platoDetalle.pk).exists()
    if existe:
        reseñasPlato = ReseñaOferta.objects.filter(oferta=platoDetalle).order_by('fecha')
    if not existe:
        reseñasPlato = ReseñaPlato.objects.filter(plato=platoDetalle).order_by('fecha')
    return render(request, 'plato/plato_detalles.html', {
            'plato': platoDetalle,
            'reseñas': reseñasPlato
        })