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
        return redirect('consumidor-home')

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
        return redirect('restaurante-home')

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "users/login.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_consumidor:
                return reverse('consumidor-home')
            elif user.is_restaurante:
                return reverse('restaurante-home')
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
