from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Plato.models import Oferta
from Usuarios.models import Consumidor
from .models import Favorito

# Create your views here.

def agregarOfertaFavoritos(request, oferta_id):
    if request.method == 'POST':
        ofertaParaAgregar = get_object_or_404(Oferta, pk=oferta_id)
        consumidorAgregar = get_object_or_404(Consumidor, Nombre=request.user.Consumidor)

        existeOfertaEnFavoritos = Favorito.objects.filter(consumidor=consumidorAgregar, oferta=ofertaParaAgregar).exists()
        
        if existeOfertaEnFavoritos:
            return HttpResponse('La oferta que tratas de agregar ya existe en tus favoritos')
        if not existeOfertaEnFavoritos:
            nuevoFavorito = Favorito(consumidor=consumidorAgregar, oferta=ofertaParaAgregar)
            nuevoFavorito.save()

        return redirect('busqueda')

def obtenerFavoritos(request):
    if request.method == 'GET':
        consumidorActual = get_object_or_404(Consumidor, Nombre=request.user.Consumidor)
        ofertasFavoritas = Favorito.objects.filter(consumidor=consumidorActual).values('oferta')
        ofertasFavoritasListado = Oferta.objects.filter(id__in=ofertasFavoritas)
        return render(request, 'ofertas/ofertas_favoritas.html', {
            'ofertasFavoritas': ofertasFavoritasListado
        })
        
def eliminarOfertaDeFavoritos(request, oferta_id):
    if request.method == 'POST':
        consumidorActual = get_object_or_404(Consumidor, Nombre=request.user.Consumidor)
        ofertaParaEliminar = get_object_or_404(Oferta, pk=oferta_id)
        ofertaFavoritaParaEliminar = Favorito.objects.filter(consumidor=consumidorActual, oferta=ofertaParaEliminar)
        ofertaFavoritaParaEliminar.first().delete()

        return redirect('busqueda')
    