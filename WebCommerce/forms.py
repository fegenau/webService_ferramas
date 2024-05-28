# Formularios (forms.py)
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=100)
    password = forms.CharField(label="Contraseña", max_length=100, widget=forms.PasswordInput)

from django import forms
from .models import Pedidos

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['estado'] 
