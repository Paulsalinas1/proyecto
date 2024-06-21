from django.shortcuts import render
from .models import producto
from django.shortcuts import get_object_or_404, redirect
from datetime import date
from .forms import ProductoForm
from os import remove, path
from django.conf import settings
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request,'vet/index.html')

def tienda(request):
    return render(request,'vet/tienda.html')

def carrito_login(request):
    return render(request,'vet/carrito_login.html')

def compras(request):
    return render(request,'vet/compras.html')

def compras_login(request):
    return render(request,'vet/compras_login.html')

def index_login(request):
    return render(request,'vet/index_login.html')

def index_trabajador(request):
    return render(request,'vet/index_trabajador.html')

def mi_cuenta(request):
    return render(request,'vet/mi_cuenta.html')

def recordando(request):
    return render(request,'vet/recordando.html')

def recordando_tienda(request):
    return render(request,'vet/recordando_tienda.html')

def Revision_estado(request):
    return render(request,'vet/Revision_estado.html')

def tienda_trabajador(request):
    prod=producto.objects.all()
    datos={
        "productos":prod  
        
    }
    
    return render(request,'vet/tienda_trabajador.html', datos)

def trabajador(request):
    return render(request,'vet/trabajador.html')

def usuarios_admin(request):
    return render(request,'vet/usuarios_admin.html')

def login(request):
    return render(request,'vet/login.html')

def login_tienda(request):
    return render(request,'vet/login_tienda.html')

def tienda_login(request):
    prod=producto.objects.all()
    datos={
        "productos":prod  
        
    }
    return render(request,'vet/tienda_login.html' , datos)

def registro(request):
     return render(request,'vet/registro.html')

def registro_tienda(request):
    return render(request,'vet/registro_tienda.html')


def crearproducto(request):
    form=ProductoForm()
    if request.method=="POST":
        form=ProductoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="tienda_trabajador")
            #Redirigir
    datos={
        "form":form
    }
    return render(request,'vet/añadir_trabajador.html',datos)