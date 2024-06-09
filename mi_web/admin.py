from django.contrib import admin
from .models import producto
# Register your models here.

class admProducto(admin.ModelAdmin):
    list_display = ['id' ,'nombre','stock']
    #list_editable
    
    

# Register your models here.
admin.site.register(producto, admProducto)