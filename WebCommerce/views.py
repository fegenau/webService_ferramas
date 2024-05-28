# Vistas (views.py)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from .models import *


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('../base')  
        else:
            return render(request, 'InicioSesion/login.html', {'error_message': 'Invalid email or password'})
    else:
        return render(request, 'InicioSesion/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  

from .models import Usuarios

def user_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        rol = request.POST.get('rol')  # Añadido
        direccion = request.POST.get('direccion')  # Añadido
        telefono = request.POST.get('telefono')  # Añadido
        rut = request.POST.get('rut')  # Añadido
        
        if password != confirm_password:
            return render(request, 'InicioSesion/register.html', {'error_message': 'Passwords do not match'})
        
        # Crear usuario en la tabla User
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()
        
        # Crear registro en la tabla Usuarios
        usuario = Usuarios(nombre=name, rut=rut, correo_electronico=email, rol=rol, direccion=direccion, telefono=telefono)
        usuario.save()
        
        return redirect('../login')  
        
    else:
        return render(request, 'InicioSesion/register.html')


from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Pedidos

def buscar_pedido(request):
    pedidos = None
    if 'cliente_rut' in request.GET:
        cliente_rut = request.GET['cliente_rut']
        pedidos = Pedidos.objects.filter(usuario_id__rut=cliente_rut)

    elif 'estado_pedido' in request.GET:
        estado_pedido = request.GET['estado_pedido']
        pedidos = Pedidos.objects.filter(estado=estado_pedido)

    return render(request, 'Vista_Bodeguero/buscar_pedido.html', {'pedidos': pedidos})







# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def anclajes (request):
    return render(request,'Anclajes/anclajes-tornillos.html')

def crearCuenta(request):
    return render(request,'CrearCuenta/crearCuenta.html')

def equipoSeguridad(request):
    return render(request,'EquiposSeguridad/equipoSeguridad.html')

def fijacion(request):
    return render(request,'Fijaciones/fijaciones.html')

def herramientas(request):
    return render(request,'Herramientas/manuales.html')

def inicioSesion (request):
    return render(request,'InicioSesion/inicioSesion.html')

def materialesBasicos(request):
    return render(request,'MaterialesBasicos/materialesBasicos.html')

def pago(request):
    return render(request,'Pago/pago.html')

def suscripcion(request):
    return render(request,'Suscripcion/suscripcion.html')