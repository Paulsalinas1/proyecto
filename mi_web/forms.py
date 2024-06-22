from django import forms
from .models import producto
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

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