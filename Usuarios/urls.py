from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path,include

urlpatterns = [
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('busqueda/', views.barraBusqueda),
    path("", views.consumidor_home, name='consumidor-home'),
    path("restaurante/", views.restaurante_home, name="restaurante-home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/consumidor/", views.ConsumidorSignUpView.as_view(), name="consumidor-signup"),
    path("signup/restaurante/", views.RestauranteSignUpView.as_view(), name="restaurante-signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
]