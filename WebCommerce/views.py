from django.shortcuts import render
from django.http import HttpResponse

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