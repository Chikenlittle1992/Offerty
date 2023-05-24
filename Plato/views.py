from django.shortcuts import render, get_object_or_404
from .models import plato, Oferta
from django.db.models import Prefetch
from Calificaciones.models import ReseñaOferta, ReseñaPlato
from Calificaciones.views import crearNuevaReseñaPlato
from Usuarios.models import Restaurante
from .forms import PlatoForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import PlatoForm, OfertaForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import plato, Oferta
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


def crear_plato_oferta(request):
    restaurante = Restaurante.objects.get(Nombre_Marca=request.user)
    platoss = plato.objects.filter(restaurant=restaurante)
    ofertass = Oferta.objects.filter(restaurant=restaurante)

    consulta={ 'platoss':platoss, 'ofertass':ofertass }
    
    if request.method == 'POST':
        form = PlatoForm(request.POST, request.FILES)
        formO = OfertaForm(request.POST, request.FILES)

        if form.is_valid() or formO.is_valid():
            if formO.is_valid():
                formO.save()
                return redirect('Plato:menu')
            if form.is_valid():
                form.save()
                return redirect('Plato:menu')  

    else:
        form = PlatoForm()
        formO = OfertaForm()

    return render(request, 'plato/menu.html', {'form': form, 'formO': formO,'consulta':consulta})

def editPlato(request, plato_id):
    plato_obj = get_object_or_404(plato, id=plato_id)

    if request.method == 'POST':
        editar = PlatoForm(request.POST, instance=plato_obj)
        if editar.is_valid():
            editar.save()
            return redirect('Plato:menu')
    else:
        editar = PlatoForm(instance=plato_obj)

    return render(request, 'plato/editar_plato.html', {'editar': editar})

def editOferta(request, plato_id):
    oferta_obj = get_object_or_404(Oferta, id=plato_id)

    if request.method == 'POST':
        editar_form = OfertaForm(request.POST, instance=oferta_obj)
        if editar_form.is_valid():
            editar_form.save()
            # Redireccionar a la página de detalles del plato actualizado
            return redirect('Plato:menu')
    else:
        editar_form = OfertaForm(instance=oferta_obj)

    return render(request, 'plato/editar_oferta.html', {'editar_form': editar_form})

def eliminarPLato(request, plato_id):
    plato_obj = get_object_or_404(plato, id=plato_id)
    plato_obj.delete()    
    return redirect('Plato:menu')
def eliminarOferta(request, plato_id):
    oferta_obj = get_object_or_404(Oferta, id=plato_id)
    oferta_obj.delete()    
    return redirect('Plato:menu')
