from django import forms
from .models import *

class contacto_form (forms.Form):
    correo = forms.EmailField(widget = forms.TextInput())
    titulo = forms.CharField(widget = forms.TextInput())
    texto  = forms.CharField(widget = forms.Textarea())


class agregar_producto_form(forms.ModelForm):
    class Meta:
        model  = Producto
        fields = '__all__'
        # fields = ['nombre','descripcion', 'precio', 'foto', 'cantidad' ]
        # exclude = ['foto']


class login_form (forms.Form):
    usuario = forms.CharField(widget = forms.TextInput())
    clave   = forms.CharField(widget = forms.PasswordInput(render_value = False))
    