from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login),
    path('register/', views.register),




    path('', views.index),
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
