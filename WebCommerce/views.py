# Vistas (views.py)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirige al usuario a una página después del inicio de sesión
            return redirect('dashboard')  # Cambia 'dashboard' por la URL a la que quieras redirigir
        else:
            # El usuario no pudo iniciar sesión, puedes mostrar un mensaje de error
            return render(request, 'InicioSesion/login.html', {'error_message': 'Invalid email or password'})
    else:
        return render(request, 'InicioSesion/login.html')



def user_logout(request):
    logout(request)
    return redirect('login')  # Redirige a la página de inicio de sesión después del cierre de sesión

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la página de inicio de sesión después del registro exitoso
    else:
        form = UserCreationForm()
    return render(request, 'InicioSesion/register.html', {'form': form})

#Ferramax

#def login(request):
#    return render(request,'InicioSesion/login.html')
#def register(request):
#    return render(request,'InicioSesion/register.html')













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