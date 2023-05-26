from django.urls import path
from Ofertas import views
from Usuarios import views as viewsUsuarios

app_name = 'Ofertas'

urlpatterns = [
    path('ofertaFavoritos/<int:oferta_id>/', views.agregarOfertaFavoritos, name='ofertaFavoritos'),
    path('eliminarFavorito/<int:oferta_id>/', views.eliminarOfertaDeFavoritos, name='eliminarFavorito'),
    path('busqueda/', viewsUsuarios.barraBusqueda, name='busqueda'),
    path('favoritos/', views.obtenerFavoritos, name='favoritos'),
]
