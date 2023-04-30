from . import views
from django.urls import path,include

urlpatterns = [
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('busqueda/', views.barraBusqueda),
    
]