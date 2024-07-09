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
    
    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        # Filtrando las opciones del campo estado
        estados_filtrados = ['preparando', 'enviado']
        self.fields['estado'].choices = [choice for choice in Pedidos.ESTADOS if choice[0] in estados_filtrados]

class PedidoForm2(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['estado']
    
    def __init__(self, *args, **kwargs):
        super(PedidoForm2, self).__init__(*args, **kwargs)
        # Filtrando las opciones del campo estado
        estados_filtrados = ['rechazado', 'cancelado', 'entregado']
        self.fields['estado'].choices = [choice for choice in Pedidos.ESTADOS if choice[0] in estados_filtrados]