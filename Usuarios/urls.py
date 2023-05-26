from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile_restaurante/', views.profile_consumidor, name='profile_restaurante'),
    path('edit_profile_restaurante/',views.edit_profile_restaurante,name='edit_profile_restaurante'),
    path('profile_consumidor/', views.profile_consumidor, name='profile_consumidor'),
    path('edit_profile_consumidor/',views.edit_profile_consumidor,name='edit_profile_consumidor'),
    path('busqueda/', views.barraBusqueda, name='busqueda'),
    path("", views.consumidor_home, name='consumidor-home'),
    path("restaurante/", views.restaurante_home, name="restaurante-home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/consumidor/", views.ConsumidorSignUpView.as_view(), name="consumidor-signup"),
    path("signup/restaurante/", views.RestauranteSignUpView.as_view(), name="restaurante-signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
]
