"""
URL configuration for sitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path , include
from . import views  

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('carrito_login/',views.carrito_login,name='carrito_login'),
    path('compras/',views.compras,name='compras'),

    
    path('index_trabajador/',views.index_trabajador,name='index_trabajador'),
    
    path('recordando/',views.recordando,name='recordando'),
    
    path('Revision_estado/',views.Revision_estado,name='Revision_estado'),
    path('tienda_trabajador/',views.tienda_trabajador,name='tienda_trabajador'),
    path('trabajador/',views.trabajador,name='trabajador'),
    path('usuarios_admin/',views.usuarios_admin,name='usuarios_admin'),
    
    path('login/',views.login_xd,name='login'),
    path('tienda_login/',views.tienda_login,name='tienda_login'),
    path('detalleP_trabajador/<id>',views.detalleP_trabajador,name='detalleP_trabajador'),
    path('eliminarP_trabajador/<id>',views.eliminarP_trabajador,name='eliminarP_trabajador'),
    path('cerrar/',views.cerrar,name='cerrar'),
    
    path('registro/',views.registro,name='registro'),
    path('mi_cuenta/<id>',views.mi_cuenta,name='mi_cuenta'),
    path('mi_cuenta_td/<id>/<usuario>',views.mi_cuenta_td,name='mi_cuenta_td'),
    
    
    path('agregar_al_carrito/<id>',views.agregar_al_carrito,name='agregar_al_carrito'),
    path('carrito/contenido/', views.contenido_carrito, name='contenido_carrito'),
    path('carrito/contenido/', views.contenido_carrito, name='contenido_carrito'),
    
    path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/actualizar_cantidad/<int:item_id>/<int:nueva_cantidad>/', views.actualizar_cantidad, name='actualizar_cantidad'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
