from django.shortcuts import render

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
    return render(request,'vet/tienda_trabajador.html')

def trabajador(request):
    return render(request,'vet/trabajador.html')

def usuarios_admin(request):
    return render(request,'vet/usuarios_admin.html')



# def login(request):
#     return render(request,'vet/login.html')

# def login_tienda(request):
#     return render(request,'vet/login_tienda.html')

# def tienda_login(request):
#     return render(request,'vet/tienda_login.html')

# def registro(request):
#     return render(request,'vet/registro.html')

# def registro_tienda(request):
#     return render(request,'vet/registro_tienda.html')