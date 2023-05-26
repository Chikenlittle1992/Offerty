from django.urls import path
from Plato import views


app_name = 'Plato'

urlpatterns = [
    path('plato/<int:plato_id>/', views.platoDetalles, name='platoDetalles'),
    path('menu/', views.crear_plato_oferta, name='menu'),
    path('editar-plato/<int:plato_id>/', views.editPlato, name='editar_plato'),
    path('editar-oferta/<int:plato_id>/', views.editOferta, name='editar_oferta'),
    path('delete_plato/<int:plato_id>', views.eliminarPLato,name="delete_plato"),
    path('delete_oferta/<int:plato_id>', views.eliminarOferta,name="delete_oferta"),
]