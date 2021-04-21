from django.urls import path 
from .views import *

urlpatterns = [
    path('', inicio_view, name='inicio_view'),
    path('about/', about_view, name='about_view'),
    path('contacto/', contacto_view, name='contacto_view'),
    path('servicios/', servicios_view, name='servicios_view'),

    path('productos/', productos_view, name='productos_view'),
    path('agregar_producto/', agregar_producto_view, name='agregar_producto'),
]