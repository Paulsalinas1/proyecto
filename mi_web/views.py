from django.shortcuts import render
from .models import producto , Usuario
from django.shortcuts import get_object_or_404, redirect
from datetime import date
from .forms import ProductoForm ,upProductoForm , loginForm , createUser ,TarjetaForm ,updateUser , upPassUser
from os import remove, path
from django.conf import settings
from django.contrib.auth import logout , login , authenticate ,update_session_auth_hash
from django.db import IntegrityError 
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request,'vet/index.html')

def carrito_login(request):
    return render(request,'vet/carrito_login.html')

def compras(request):
    return render(request,'vet/compras.html')

def index_trabajador(request):
    return render(request,'vet/index_trabajador.html')

def mi_cuenta(request, id):
    usera=get_object_or_404(Usuario,correo=id)
    form=updateUser(instance=usera) 
    form2=upPassUser(user=request.user)
    
    if request.method=="POST":
            form=updateUser(data=request.POST,files=request.FILES,instance=usera)
            form2=upPassUser(data=request.POST,files=request.FILES,user=request.user)
            if 'update_profile' and 'change_password'in request.POST:
                if  form.is_valid() and form2.is_valid():
                    form.save()
                    form2.save()
                    update_session_auth_hash(request, form2.user)  # Mantener al usuario autenticado después del cambio de contraseña
                    return redirect(reverse("mi_cuenta",args=[id]))
            if 'update_profile' in request.POST:         
                if  form.is_valid():  
                    form.save()
                    return redirect(reverse("mi_cuenta",args=[id]))
            if 'change_password' in request.POST:          
                if  form2.is_valid():
                    form2.save()    
                    update_session_auth_hash(request, form2.user)  # Mantener al usuario autenticado después del cambio de contraseña  
                    return redirect(reverse("mi_cuenta",args=[id]))     
    datos={
        "form":form, 
        "form2":form2   
    }
    return render(request,'vet/mi_cuenta.html' , datos)

def recordando(request):
    return render(request,'vet/recordando.html')

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
            if user.is_staff:
                return redirect("trabajador")
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
    prod=producto.objects.all()
    datos={
        "productos":prod 
    }
    return render(request,'vet/tienda_login.html',datos)

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
    form2= TarjetaForm()
    
    if request.method=="POST":
        form=createUser(data=request.POST)
        form2=TarjetaForm(data=request.POST)
        
        if form.is_valid():
            usuario=form.save()
            
            if form2.is_valid():
                tarjeta = form2.save(commit=False)
                tarjeta.uusuario=usuario
                tarjeta.save()
                return redirect("login")
                #Redirigir  
    datos= {
        "form":form,
        "form2":form2
        
    }
    
    return render(request , 'vet/registro.html' , datos)

