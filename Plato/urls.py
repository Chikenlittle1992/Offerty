from django.urls import path
from Plato import views


app_name = 'Plato'

urlpatterns = [
    path('plato/<int:plato_id>/', views.platoDetalles, name='platoDetalles'),
]