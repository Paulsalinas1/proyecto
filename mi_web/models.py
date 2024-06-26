from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin 
from .enumeraciones import *
# Create your models here.

class producto(models.Model):
    nombre=models.CharField(max_length=50, null=False ,unique=True)
    stock=models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(1000)])
    descripción=models.CharField(max_length=50, null=False) 
    precio=models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(999999)])
    foto=models.ImageField(upload_to='producto',null=False)
    
    def __str__(self):
        return f"{self.nombre}"


class Usuariomanager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError("El correo es obligatorio")
        usuario = self.model(correo=self.normalize_email(correo), **extra_fields)
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(correo=correo, password=password, **extra_fields)   
    
class Usuario(AbstractBaseUser,PermissionsMixin):
    run = models.CharField( "rut" ,max_length=10 ,primary_key=True ) 
    correo = models.EmailField("correo", max_length=150 , unique=True)
    nombre = models.CharField("nombre", max_length=50)
    apellido = models.CharField("apellido", max_length=50)
    telefono= models.CharField("telefono", max_length=9)
    comuna= models.CharField("comuna", max_length=50)
    direccion= models.CharField("direccion", max_length=50)
    is_staff = models.BooleanField("empleado",default=False)
    is_superuser = models.BooleanField("superuser",default=False)
    
    USERNAME_FIELD="correo"
    objects=Usuariomanager()
    REQUIRED_FIELDS=["run","nombre","apellido","telefono","comuna","direccion"]

class Tarjeta(models.Model):  
    uusuario=models.ForeignKey("mi_web.Usuario", verbose_name=("usuario"), on_delete=models.CASCADE , null=True)
    tarjeta_de_credito = models.IntegerField("numero tarjeta", unique=True)
    fecha_de_vencimiento = models.CharField("fecha vencimiento", max_length=50)
    codigo_de_seguridad = models.IntegerField("cv")
    


class CarritoDeCompras(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE )
    productos = models.ManyToManyField(producto, through='ItemCarrito')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Carrito de {self.user.username}'
    

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(CarritoDeCompras, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.cantidad} of {self.producto.nombre}'
    

class Boleta(models.Model):
    user = models.OneToOneField(Usuario, verbose_name=("Usuario") ,on_delete=models.DO_NOTHING)
    carritoDeCompra = models.OneToOneField(CarritoDeCompras,verbose_name=("CarritoDeCompra") , on_delete=models.DO_NOTHING)
    metodoDePago = models.ForeignKey(Tarjeta, verbose_name=("metodoDePago") ,on_delete=models.DO_NOTHING)
    estado = models.CharField("Estado",max_length=20, choices=ESTADO_ENVIO,default="ALMACEN")
    telefono = models.CharField("Teléfono", max_length=9)
    comuna = models.CharField("Comuna", max_length=50)
    direccion = models.CharField("Dirección", max_length=50)
    fecha_emision = models.DateTimeField("fecha_emision",auto_now_add=True)
    
    def __str__(self):
        return f'Boleta {self.id} - {self.user.nombre}'
