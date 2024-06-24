from django.contrib import admin
from .models import producto , Usuario , Tarjeta
# Register your models here.

class admProducto(admin.ModelAdmin):
    list_display = ['id' ,'nombre','stock']
    #list_editable
    
    
class admUsuarios(admin.ModelAdmin):
    list_display = ['run' ,'nombre','correo']
    #list_editable

class admTarjeta(admin.ModelAdmin):
    list_display = ['tarjeta_de_credito' , 'uusuario']
    #list_editable    
# Register your models here.
admin.site.register(producto, admProducto)

admin.site.register(Usuario, admUsuarios)

admin.site.register(Tarjeta, admTarjeta)