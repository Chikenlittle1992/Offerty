from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User
from .forms import ConsumidorSignUpForm, RestauranteSignUpForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import consumidor_requerido, restaurante_requerido
from .forms import *
from django.contrib.auth.decorators import login_required
from Plato import models as modelosPlato
from django.db.models import Q

# Create your views here.
def barraBusqueda(request):
    searchTerm = request.GET.get('searchService')
    platos = modelosPlato.plato.objects.all()
    ofertas = []
    if searchTerm:
        platos = platos.filter(Q(name__icontains=searchTerm) | Q(category__icontains=searchTerm)| Q(restaurant__Nombre_Marca__icontains=searchTerm))
    else:
        platos = modelosPlato.plato.objects.all()
        ofertas = modelosPlato.Oferta.objects.all()
    return render(request, 'base.html', {'searchTerm': searchTerm,'ofertas': ofertas,'platos': platos})


@login_required
def edit_profile_restaurante(request):
    restaurante = Restaurante.objects.get(user = request.user)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        nombre_marca = request.POST['Nombre_Marca']
        ubicacion = request.POST['ubicacion']
        bio = request.POST['bio']
        image = request.FILES['images'] 

        user = request.user
        user.username = username
        user.email = email
        user.save()
        restaurante.Nombre_Marca = nombre_marca
        restaurante.ubicacion = ubicacion
        restaurante.bio = bio
        restaurante.image = image
        restaurante.save()
    return render(request, 'edit_profile_restaurante.html', {'user':request.user, 'restaurante':restaurante})

@login_required
def edit_profile_consumidor(request):
    consumidor = Consumidor.objects.get(user = request.user)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        Nombre = request.POST['Nombre']
        bio = request.POST['bio']
        image = request.FILES['images'] 

        user = request.user
        user.username = username
        user.email = email
        user.save()
        consumidor.Nombre = Nombre
        consumidor.bio = bio
        consumidor.image = image
        consumidor.save()
    return render(request, 'edit_profile_consumidor.html', {'user': request.user, 'consumidor': consumidor})

@login_required
def profile_restaurante(request):
    consumidor = Consumidor.objects.get(user = request.user)
    return render(request, 'profile_consumidor.html', {'user':request.user, 'consumidor':consumidor})

@login_required
def profile_consumidor(request):
    restaurante = Restaurante.objects.get(user = request.user)
    return render(request, 'profile_restaurante.html', {'user':request.user, 'restaurante':restaurante})

class ConsumidorSignUpView(CreateView):
    model = User
    form_class = ConsumidorSignUpForm
    template_name = 'users/consumidor-signup.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'consumidor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('busqueda')

class RestauranteSignUpView(CreateView):
    model = User
    form_class = RestauranteSignUpForm
    template_name = 'users/restaurante-signup.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'restaurante'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('busqueda')

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "users/login.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            #if user.is_consumidor:
            return reverse('busqueda')
            #elif user.is_restaurante:
                #return reverse('restaurante-home')
        else: 
            return reverse('login')

@login_required
@consumidor_requerido
def consumidor_home(request):
    return render(request, 'users/consumidor-home.html')

@login_required
@restaurante_requerido
def restaurante_home(request):
    return render(request, 'users/restaurante-home.html')
