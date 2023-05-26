from django.urls import path
from Calificaciones import views
from Usuarios import views as viewsUsuarios

app_name = 'Calificaciones'

urlpatterns = [
    path('crearReseñaPlato/<int:plato_id>/', views.crearNuevaReseñaPlato, name='crearReseñaPlato'),
    path('crearReseñaRestaurante/<str:restaurante_nombre>/', views.crearNuevaReseñaRestaurante, name='crearReseñaRestaurante'),
    path('crearReseñaApp/', views.crearNuevaReseñaApp, name='crearReseñaApp'),
    path('busqueda/', viewsUsuarios.barraBusqueda, name='busqueda'),
]
