# Vistas (views.py)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  
        else:
            return render(request, 'InicioSesion/login.html', {'error_message': 'Invalid email or password'})
    else:
        return render(request, 'InicioSesion/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')  

def user_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            return render(request, 'InicioSesion/register.html', {'error_message': 'Passwords do not match'})
        
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()
        
        return redirect('login')  
        
    else:
        return render(request, 'InicioSesion/register.html')


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