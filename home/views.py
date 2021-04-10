from django.shortcuts import render
from .forms import *
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