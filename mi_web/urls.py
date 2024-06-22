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
    path('tienda/',views.tienda,name='tienda'),
    path('carrito_login/',views.carrito_login,name='carrito_login'),
    path('compras/',views.compras,name='compras'),
    path('compras_login/',views.compras_login,name='compras_login'),
    path('index_login/',views.index_login,name='index_login'),
    path('index_trabajador/',views.index_trabajador,name='index_trabajador'),
    path('mi_cuenta/',views.mi_cuenta,name='mi_cuenta'),
    path('recordando/',views.recordando,name='recordando'),
    path('recordando_tienda/',views.recordando_tienda,name='recordando_tienda'),
    path('Revision_estado/',views.Revision_estado,name='Revision_estado'),
    path('tienda_trabajador/',views.tienda_trabajador,name='tienda_trabajador'),
    path('trabajador/',views.trabajador,name='trabajador'),
    path('usuarios_admin/',views.usuarios_admin,name='usuarios_admin'),
    path('registro/',views.registro,name='registro'),
    path('registro_tienda/',views.registro_tienda,name='registro_tienda'),
    path('login/',views.login,name='login'),
    path('login_tienda/',views.login_tienda,name='login_tienda'),
    path('tienda_login/',views.tienda_login,name='tienda_login'),
    
    path('detalleP_trabajador/<id>',views.detalleP_trabajador,name='detalleP_trabajador'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
