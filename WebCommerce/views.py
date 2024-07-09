# Vistas (views.py)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from .models import *
from django.db.models import Q
from .forms import *

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

def buscar_pedido(request):
    pedidos = None
    if 'cliente_rut' in request.GET:
        cliente_rut = request.GET['cliente_rut']
        pedidos = Pedidos.objects.filter(usuario_id__rut=cliente_rut, estado__in=['aprobado', 'preparando'])
    elif 'estado_pedido' in request.GET:
        estado_pedido = request.GET['estado_pedido']
        if estado_pedido in ['aprobado', 'preparando']:
            pedidos = Pedidos.objects.filter(estado=estado_pedido)

    return render(request, 'Vista_Bodeguero/buscar_pedido.html', {'pedidos': pedidos})

def buscar_pedido2(request):
    pedidos = None
    if 'cliente_rut' in request.GET:
        cliente_rut = request.GET['cliente_rut']
        pedidos = Pedidos.objects.filter(usuario_id__rut=cliente_rut, estado__in=['pendiente', 'enviado'])
    elif 'estado_pedido' in request.GET:
        estado_pedido = request.GET['estado_pedido']
        if estado_pedido in ['pendiente', 'enviado']:
            pedidos = Pedidos.objects.filter(estado=estado_pedido)

    return render(request, 'Vista_Vendedor/buscar_pedido2.html', {'pedidos': pedidos})

def modificar_pedido2(request, pedido_id):
    pedido = get_object_or_404(Pedidos, pk=pedido_id)
    if request.method == 'POST':
        form = PedidoForm2(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('buscar_pedido2')
    else:
        form = PedidoForm2(instance=pedido)
    return render(request, 'Vista_Vendedor/modificar_pedido2.html', {'form': form, 'pedido': pedido})


def modificar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedidos, pk=pedido_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('buscar_pedido', )
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'Vista_Bodeguero/modificar_pedido.html', {'form': form, 'pedido': pedido})

<<<<<<< HEAD
# Catalogo
def herramientasmanuales(request):
    return render(request, 'catalogo/herramientasmanuales.html')
def equiposmedicion(request):
    return render(request, 'catalogo/equiposmedicion.html')
def equiposseguridad(request):
    return render(request, 'catalogo/equiposseguridad.html')
def fijaciones(request):
    return render(request, 'catalogo/fijaciones.html')
def materialesbasicos(request):
    return render(request, 'catalogo/materialesbasicos.html')
def tornillosanclajes(request):
    return render(request, 'catalogo/tornillosanclajes.html')
=======

<<<<<<< HEAD
from django.shortcuts import render
from django.db.models import Q
from .models import Productos, Categorias, Marcas
>>>>>>> unreleased
=======
>>>>>>> unreleased

def productos_disponibles(request):
    query = request.GET.get('q', '')
    productos = Productos.objects.filter(stock__gt=0)

    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) |
            Q(marca_id__nombre__icontains=query) |
            Q(categoria_id__nombre__icontains=query)
        )

    return render(request, 'Vista_Vendedor/productos_disponibles.html', {'productos': productos, 'query': query})





















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