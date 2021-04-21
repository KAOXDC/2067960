from django.shortcuts import render, redirect
from .forms import *
from .models import Producto, Marca, Categoria

# Create your views here.
def inicio_view(request):
    msg = 'esta es la pagina de incio'
    return render(request, 'inicio.html', locals())
def about_view(request):
    return render(request, 'about.html')

def contacto_view(request):
    c = ""
    a = ""
    t = ""
    enviado = False
    if request.method == 'POST':
        formulario = contacto_form(request.POST)
        if formulario.is_valid():
            enviado = True
            c = formulario.cleaned_data['correo']
            a = formulario.cleaned_data['titulo']
            t = formulario.cleaned_data['texto']
    else: #GET
        formulario = contacto_form()
    
    return render(request, 'contacto.html', locals())

def servicios_view (request):
    return render(request, "servicios.html", locals())

def productos_view (request):
    productos = Producto.objects.filter(activo=True) # SELECT * FROM 'Producto' WHERE activo=1;

    return render(request, 'productos.html', locals())

def agregar_producto_view (request):
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/productos/')
    else: #GET
        formulario = agregar_producto_form()
    return render (request, 'agregar_producto.html', locals())