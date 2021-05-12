from django.urls import path 
from .views import *

urlpatterns = [
    path('', inicio_view, name='inicio_view'),
    path('about/', about_view, name='about_view'),
    path('contacto/', contacto_view, name='contacto_view'),
    path('servicios/', servicios_view, name='servicios_view'),

    path('productos/', productos_view, name='productos_view'),
    path('agregar_producto/', agregar_producto_view, name='agregar_producto'),
    path('ver_producto/<int:id_prod>', ver_producto_view, name='ver_producto'),
    path('eliminar_producto/<int:id_prod>', eliminar_producto_view, name='eliminar_producto'),
    path('editar_producto/<int:id_prod>', editar_producto_view, name='editar_producto'),

    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('register/', register_view, name='register_view'),

]