from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.db import transaction
from django import forms
from .models import User, Consumidor, Restaurante
from django.contrib.auth import get_user_model

User = get_user_model()

class ConsumidorSignUpForm(UserCreationForm):
    email = forms.EmailField(widget =forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    Nombre = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_consumidor = True
        if commit:
            user.save()
        consumidor = Consumidor.objects.create(user=user, Nombre = self.cleaned_data.get('Nombre'))
        return user

class RestauranteSignUpForm(UserCreationForm):
    email = forms.EmailField(widget =forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    Nombre_Marca = forms.CharField(widget=forms.TextInput())
    ubicacion = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_restaurante = True
        if commit:
            user.save()
        restaurante = Restaurante.objects.create(user=user, Nombre_Marca = self.cleaned_data.get('Nombre_Marca'), ubicacion = self.cleaned_data.get('ubicacion'))
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
