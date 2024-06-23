from django.shortcuts import render
from .models import producto
from django.shortcuts import get_object_or_404, redirect
from datetime import date
from .forms import ProductoForm ,upProductoForm , loginForm , createUser ,targetaForm
from os import remove, path
from django.conf import settings
from django.contrib.auth import logout , login , authenticate 
from django.db import IntegrityError 
from django.contrib import messages


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

def login_xd(request):
    if request.method=="POST":
        form = loginForm(data=request.POST)
        if form.is_valid():
            user = form.user_cache
              
            login(request ,user)
            return redirect("index")
        else :
            messages.warning(request, "usuario o contraseña incorrectos") 
            return redirect("login")
    else :
        form = loginForm()
    datos ={
        "form":form
    }
    return render(request,'vet/login.html',datos)

def login_tienda(request):
    return render(request,'vet/login_tienda.html')


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
    imagen_anterior = produc.foto.path if produc.foto else None
    
    if request.method=="POST":
            form=upProductoForm(data=request.POST,files=request.FILES,instance=produc)
            if form.is_valid():
                imagen_nueva = form.cleaned_data.get('foto')
                if imagen_nueva and imagen_anterior:
                # Comprobar si la nueva imagen es diferente de la anterior
                    if imagen_nueva.name != path.basename(imagen_anterior):
                    # Eliminar la imagen anterior
                        if path.exists(imagen_anterior):
                            remove(imagen_anterior)
                    
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

def cerrar(request):
    logout(request)
    return redirect("index") 

def registro(request):
    form = createUser()
    form2= targetaForm()
    
    if request.method=="POST":
        form=createUser(data=request.POST)
        form2=targetaForm(data=request.POST)
        if form2.is_valid():
            tarjeta = form2.save()
            
            if form.is_valid():
                usuario=form.save(commit=False)
                usuario.tarjeta= tarjeta
                usuario.save()
                return redirect("login")
            #Redirigir  
    datos= {
        "form":form,
        "form2":form2
    }
    
    return render(request , 'vet/registro.html' , datos)




     