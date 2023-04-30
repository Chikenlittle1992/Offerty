from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from django import forms
from .models import User, Consumidor, Restaurante
from django.contrib.auth import get_user_model

User = get_user_model()

class ConsumidorSignUpForm(UserCreationForm):
    email = forms

class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)    
    class Meta:
        model = User
        fields = ['email']