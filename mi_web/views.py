from django.shortcuts import render
from .models import producto
from django.shortcuts import get_object_or_404, redirect
from datetime import date
from .forms import ProductoForm ,upProductoForm
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



def trabajador(request):
    return render(request,'vet/trabajador.html')

def usuarios_admin(request):
    return render(request,'vet/usuarios_admin.html')

def login(request):
    return render(request,'vet/login.html')

def login_tienda(request):
    return render(request,'vet/login_tienda.html')


def registro(request):
     return render(request,'vet/registro.html')

def registro_tienda(request):
    return render(request,'vet/registro_tienda.html')


def tienda_trabajador(request):
    prod=producto.objects.all()
    form=ProductoForm()
    
    if request.method=="POST":
        form=ProductoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="tienda_trabajador")
            #Redirigir       
    datos={
        "productos":prod ,
        "form2":form 
    }
    return render(request,'vet/tienda_trabajador.html',datos)

def tienda_login(request):
    return render(request,'vet/tienda_trabajador.html')


def detalleP_trabajador(request, id):
    produc=get_object_or_404(producto,nombre= id)
    form=upProductoForm(instance=produc)
    
    if request.method=="POST":
            form=upProductoForm(data=request.POST,files=request.FILES,instance=produc)
            if form.is_valid():
                form.save()
                return redirect(to="tienda_trabajador")
            
    datos={
        "form":form ,
        "pro":produc
    }
    
    return render(request,'vet/detalleP_trabajador.html',datos)

def eliminarP_trabajador(request, id):
    produc=get_object_or_404(producto,nombre= id)
    form=upProductoForm(instance=produc)
    
    if request.method=="POST":
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media',''))+produc.foto.url)
            produc.delete()
            return redirect(to="tienda_trabajador")
            
    datos={
        "form":form ,
        "pro":produc
    }
    
    return render(request,'vet/eliminarP_trabajador.html',datos)
