from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Calificaciones.forms import CreacionNuevaReseñaPlato
from Usuarios.models import Consumidor
from Plato.models import plato



# Create your views here.

# Create your views here.
def crearNuevaReseñaPlato(request, plato_id):
    if request.method == 'GET':
        platoReseñar = get_object_or_404(plato, pk=plato_id)
        form = CreacionNuevaReseñaPlato(initial={
            'consumidor': Consumidor.objects.get(Nombre=request.user.Consumidor),
            'plato': platoReseñar
        })
        return render(request, 'calificaciones/nueva_reseña.html', {
            'form': form,
            'plato': platoReseñar
        })
    if request.method == 'POST':
        form = CreacionNuevaReseñaPlato(request.POST)
        try:
            form.save()
            return HttpResponse('Creada')
        except:
            return HttpResponse('Fallo')