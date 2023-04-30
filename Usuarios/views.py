from django.shortcuts import render
from .forms import EditProfileForm
from django.contrib.auth.decorators import login_required
from Plato import models as modelosPlato
from django.db.models import Q

# Create your views here.
def barraBusqueda(request):
    searchTerm = request.GET.get('searchService')
    platos = modelosPlato.plato.objects.all()
    if searchTerm:
        platos = platos.filter(Q(name__icontains=searchTerm) | Q(category__icontains=searchTerm)| Q(restaurant__Nombre_Marca__icontains=searchTerm))
    else:
        platos = modelosPlato.plato.objects.all()
    return render(request, 'base.html', {'searchTerm': searchTerm, 'platos': platos})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})
