from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Calificaciones.forms import CreacionNuevaReseñaPlato, CreacionNuevaReseñaOferta
from Usuarios.models import Consumidor
from Plato.models import plato, Oferta

# Create your views here.

# Create your views here.
def crearNuevaReseñaPlato(request, plato_id):
    platoReseñar = get_object_or_404(plato, pk=plato_id)
    platoEsOferta = Oferta.objects.filter(pk=platoReseñar.pk).exists()
    if request.method == 'GET':
        if platoEsOferta:
            form = CreacionNuevaReseñaOferta()
        if not platoEsOferta:
            form = CreacionNuevaReseñaPlato()
        
        return render(request, 'calificaciones/nueva_reseña.html', {
            'form': form,
            'plato': platoReseñar,
        })
    if request.method == 'POST':
        if platoEsOferta:
            form = CreacionNuevaReseñaOferta(request.POST)
        if not platoEsOferta:
            form = CreacionNuevaReseñaPlato(request.POST)
        consumidorReseñador = get_object_or_404(Consumidor, Nombre=request.user.Consumidor)
        
        try:
            if form.is_valid():
                reseñaForm = form.save(commit=False)
                if platoEsOferta:
                    reseñaForm.oferta = get_object_or_404(Oferta, pk=plato_id)
                if not platoEsOferta:
                    reseñaForm.plato = get_object_or_404(plato, pk=plato_id)
                reseñaForm.consumidor = consumidorReseñador  # Estableces el valor por defecto
                reseñaForm.save()
                
                return redirect('busqueda')
        except:
            return HttpResponse('Hubo un error al crear la reseña')