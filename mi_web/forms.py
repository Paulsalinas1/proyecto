from django import forms
from .models import producto 
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import get_user_model

useru = get_user_model()
class ProductoForm(forms.ModelForm):
     class Meta:
         model = producto
         fields = ['nombre','stock','descripción','precio','foto']
         
         
class upProductoForm(forms.ModelForm):
     class Meta:
         model = producto
         fields = ['nombre','stock','descripción','precio','foto']
         
         
         
class loginForm(AuthenticationForm):
    pass


class createUser(UserCreationForm):
    class Meta:
        model = useru
        fields =["correo","run","nombre","apellido","telefono","comuna","direccion"]

