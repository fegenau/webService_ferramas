from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index),
    path('login/', views.user_login,name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('index/', views.index, name='index'),


    path('buscar_pedido/', views.buscar_pedido, name='buscar_pedido'),
    path('modificar_pedido/<int:pedido_id>/', views.modificar_pedido, name='modificar_pedido'),

#catalogo
    path('catalogo/herramientasmanuales/', views.herramientasmanuales, name='herramientasmanuales'),
    path('equiposmedicion/', views.equiposmedicion, name='equiposmedicion'),
    path('equiposseguridad/', views.equiposseguridad, name='equiposseguridad'),
    path('fijaciones/', views.fijaciones, name='fijaciones'),
    path('materialesbasicos/', views.materialesbasicos, name='materialesbasicos'),
    path('tornillosanclajes/', views.tornillosanclajes, name='tornillosanclajes'),

    path('about/', views.about),
    path('anclajes/', views.anclajes),
    path('crear-cuenta/', views.crearCuenta),
    path('equipo-seguridad/', views.equipoSeguridad),
    path('fijaciones/', views.fijacion),
    path('herramientas/', views.herramientas),
    path('inicio-sesion/', views.inicioSesion),
    path('materiales-basicos',views.materialesBasicos),
    path('pago/', views.pago),
    path('suscripcion/', views.suscripcion),
    
]
