from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.http import HttpResponse
from Calificaciones.forms import CreacionNuevaReseñaPlato, CreacionNuevaReseñaOferta, CreacionNuevaReseñaRestaurante, CreacionNuevaReseñaApp
from Usuarios.models import Consumidor, Restaurante
from Calificaciones.models import ReseñaRestaurante, ReseñaApp
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
        
        return render(request, 'calificaciones/nueva_reseña_plato.html', {
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
        
def crearNuevaReseñaRestaurante(request, restaurante_nombre):
    restauranteReseñar = get_object_or_404(Restaurante, Nombre_Marca=restaurante_nombre)
    if request.method == 'GET':
        form = CreacionNuevaReseñaRestaurante()
        reseñasRestaurante = obtenerReseñasRestaurante(restaurante_nombre)

        sumaCalificacionesRestaurante = reseñasRestaurante.aggregate(total=Sum('puntaje_calificacion'))['total']
        numeroReseñasRestaurante = reseñasRestaurante.count()
        promedioCalificacionesRestaurante = sumaCalificacionesRestaurante / numeroReseñasRestaurante if numeroReseñasRestaurante > 0 else None
        
        return render(request, 'calificaciones/nueva_reseña_restaurante.html', {
            'form': form,
            'restaurante': restauranteReseñar,
            'reseñas': reseñasRestaurante,
            'promedioCalificaciones': promedioCalificacionesRestaurante,
        })
    if request.method == 'POST':
        form = CreacionNuevaReseñaRestaurante(request.POST)

        consumidorReseñador = get_object_or_404(Consumidor, Nombre=request.user.Consumidor)
        
        try:
            if form.is_valid():
                reseñaForm = form.save(commit=False)
                reseñaForm.restaurante = restauranteReseñar
                reseñaForm.consumidor = consumidorReseñador  # Estableces el valor por defecto
                reseñaForm.save()
                
                return redirect('busqueda')
        except:
            return HttpResponse('Hubo un error al crear la reseña')
        
def obtenerReseñasRestaurante(restaurante_nombre):
    restauranteActual = get_object_or_404(Restaurante, Nombre_Marca=restaurante_nombre)
    reseñasRestaurante = ReseñaRestaurante.objects.filter(restaurante=restauranteActual).order_by('-fecha')

    return reseñasRestaurante

def crearNuevaReseñaApp(request):
    if request.method == 'GET':
        form = CreacionNuevaReseñaApp()
        reseñasApp = ReseñaApp.objects.all().order_by('-fecha')

        sumaCalificacionesApp = reseñasApp.aggregate(total=Sum('puntaje_calificacion'))['total']
        numeroReseñasApp = reseñasApp.count()
        promedioCalificacionesApp = sumaCalificacionesApp / numeroReseñasApp if numeroReseñasApp > 0 else None
        
        return render(request, 'calificaciones/nueva_reseña_app.html', {
            'form': form,
            'reseñas': reseñasApp,
            'promedioCalificaciones': promedioCalificacionesApp,
        })
    if request.method == 'POST':
        form = CreacionNuevaReseñaApp(request.POST)

        consumidorReseñador = get_object_or_404(Consumidor, Nombre=request.user.Consumidor)
        
        try:
            if form.is_valid():
                reseñaForm = form.save(commit=False)
                reseñaForm.consumidor = consumidorReseñador  # Estableces el valor por defecto
                reseñaForm.save()
                
                return redirect('busqueda')
        except:
            return HttpResponse('Hubo un error al crear la reseña')