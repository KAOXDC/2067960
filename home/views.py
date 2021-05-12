from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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

def ver_producto_view (request, id_prod):

	detalle = Producto.objects.get(id = id_prod) # SELECT * FROM 'home_producto' WHERE  id == id_prod
	# get_or_404    
	# JOINS o SUBCONSULTAS para las categorias del producto 
	# Tambien se pueden hacer con querysets

	return render(request, 'ver_producto.html', locals())
 
def eliminar_producto_view (request, id_prod):
	objeto = Producto.objects.get(id = id_prod)
	objeto.delete()
	return redirect('/productos/')

def editar_producto_view (request, id_prod):
	objeto = Producto.objects.get(id = id_prod)
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST, request.FILES, instance = objeto)
		if formulario.is_valid():
			formulario.save()
			return redirect('/productos/')
	else:
		formulario = agregar_producto_form(instance = objeto )
	return render(request, 'agregar_producto.html', locals())


def login_view (request):
	usu = ''
	cla = ''
	if request.method == 'POST':
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username = usu, password=cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/')
			else:
				msj = 'usuario o clave incorrectos'
	else: #GET
		formulario = login_form()
	return render(request, 'login.html', locals()) 

def logout_view (request):
	logout(request)
	return redirect('/login/') 

def register_view (request):
	formulario = register_form()
	usu = ""
	cor = ""
	cla_1 = ""
	cla_2 =""
	if request.method=='POST':
		formulario = register_form(request.POST)
		if formulario.is_valid():
			usu   = formulario.cleaned_data['usuario']
			cor   = formulario.cleaned_data['correo']
			cla_1 = formulario.cleaned_data['clave_1']
			cla_2 = formulario.cleaned_data['clave_2']
			u = User.objects.create_user(username = usu, email=cor, password=cla_1)
			u.save()
			return redirect ('/login/')
		else:
			msj = 'no se pudo crear el usuario'			
	else:		
		return render(request, 'register.html', locals())
	return render(request, 'register.html', locals())