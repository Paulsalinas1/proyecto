from django.shortcuts import render
from .models import producto , Usuario , Tarjeta , CarritoDeCompras,ItemCarrito ,Boleta
from django.shortcuts import get_object_or_404, redirect
from datetime import date
from .forms import ProductoForm ,upProductoForm , loginForm , createUser ,TarjetaForm ,updateUser , upPassUser ,ItemCarritoForm ,BoletaForm
from os import remove, path
from django.conf import settings
from django.contrib.auth import logout , login , authenticate ,update_session_auth_hash 
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError 
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse



# Create your views here.
def index(request):
    return render(request,'vet/index.html')

def compras(request):
    return render(request,'vet/compras.html')

def index_trabajador(request):
    return render(request,'vet/index_trabajador.html')

def mi_cuenta(request, id):
    usera=get_object_or_404(Usuario,correo=id)
    form=updateUser(instance=usera) 
    form2=upPassUser(user=request.user)
    form3=Tarjeta.objects.filter(uusuario=usera)
    form4= TarjetaForm()
    Boletas = Boleta.objects.filter(user=usera)
    Boletas_completadas = Boleta.objects.filter(user=usera, estado='COMPLETADO')
    if request.method=="POST":
            form=updateUser(data=request.POST,files=request.FILES,instance=usera)
            form2=upPassUser(data=request.POST,files=request.FILES,user=request.user)
            form4=TarjetaForm(data=request.POST)
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
            if 'agragar_tarjeta' in request.POST: 
                if form4.is_valid():
                    tarjeta = form4.save(commit=False)
                    tarjeta.uusuario=usera
                    tarjeta.save() 
                    return redirect(reverse("mi_cuenta",args=[id]))       
    datos={
        "form":form, 
        "form2":form2,
        "targetas":form3,
        "form4":form4,
        "boletas":Boletas,
        "Boletas_completadas":Boletas_completadas
    }
    return render(request,'vet/mi_cuenta.html' , datos)

def mi_cuenta_td(request,id,usuario):
    tar=get_object_or_404(Tarjeta,id = id)
    form=TarjetaForm(instance=tar)
    
    if request.method=="POST":
        form=TarjetaForm(data=request.POST)
        if 'eliminar_tarjeta' in request.POST:   
            tar.delete()
            return redirect(reverse("mi_cuenta",args=[usuario])) 
        if 'modificar_tarjeta' in request.POST:  
           if form.is_valid():
                form.save()
                return redirect(reverse("mi_cuenta",args=[usuario]))  
            
    datos={
        "form":form
    }        
    return render(request,'vet/mi_cuenta_td.html' , datos)

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


def detalle_producto(request, producto_id):
    producto2 = get_object_or_404(producto, id=producto_id)
    return render(request, 'vet/detalle_producto.html', {'producto': producto2})

def agregar_producto(request, producto_id):
    producto2 = get_object_or_404(producto, id=producto_id)
    carrito, created = CarritoDeCompras.objects.get_or_create(user=request.user, is_active=True)
    
    cantidad = int(request.POST.get('cantidad', 1))
    
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto2, defaults={'cantidad': cantidad})
    if not created:
        item.cantidad += cantidad
        item.save()
    
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito, created = CarritoDeCompras.objects.get_or_create(user=request.user, is_active=True)
    carrito = get_object_or_404(CarritoDeCompras, user=request.user, is_active=True)
    
    items = ItemCarrito.objects.filter(carrito=carrito) if carrito else []
    total = sum(item.producto.precio * item.cantidad for item in items)
    return render(request, 'vet/ver_carrito.html', {'items': items, 'total': total})

def eliminar_producto(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    return redirect('ver_carrito')



def carrito_login(request):
    form = BoletaForm(user=request.user)
    carrito_de_compras = CarritoDeCompras.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = BoletaForm(request.POST,files=request.FILES,user=request.user)
        if form.is_valid():
            boleta = form.save(commit=False)
            boleta.user = request.user
            boleta.carritoDeCompra = carrito_de_compras  # Asignar el carrito de compras correspondiente
            boleta.save()
            id=boleta.id
            # Vaciar el carrito de compras del usuario
            carrito_de_compras.productos.clear()
            return redirect(reverse("ver_boleta",args=[id]))
    datos={
        "form":form
    }
    return render(request,'vet/carrito_login.html',datos)


def ver_boleta(request,id):
    boleta = get_object_or_404(Boleta, id=id)
    datos={
        "boleta":boleta
    }
    return render(request,'vet/ver_boleta.html',datos)