from typing import Any
from django import forms
from .models import producto , Tarjeta , ItemCarrito
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm ,UserChangeForm ,PasswordChangeForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout , Submit , Div ,Field 
from crispy_forms.bootstrap import PrependedText

  
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
    
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"id":"password1"}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={"id":"password2"}))
    
    class Meta:
        model = useru 
        fields =["correo","run","nombre","apellido","telefono","comuna","direccion"]

    def __init__(self, *args , **kwargs ):
        super().__init__(*args, **kwargs)
        self.helper= FormHelper()
        self.helper.form_method="post"
        self.helper.form_class="needs-validation"
        self.helper.attrs={"novalidate":""}
        self.helper.layout=Layout(
           Field("correo",id="correo") ,
           Field("run",id="Rut") ,
           Field("nombre",id="nombre"), 
           Field("apellido",id="apellido"), 
           Div(
                Div(
                    PrependedText('telefono', '+56', active=True , id="fono"),
                    css_class='input-group'
                ,id="fono2"),
                css_class='form-group'
            ),
           Field("comuna",id="comuna"), 
           Field("direccion",id="direc"), 
           Field("password1",id="contraseña"), 
           Field("password2",id="repetirContraseña")    
        )
            
        
class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ["tarjeta_de_credito", "fecha_de_vencimiento", "codigo_de_seguridad"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper= FormHelper()
        self.helper.form_method="post"
        self.helper.form_class="needs-validation"
        self.helper.attrs={"novalidate":""}
        self.fields['tarjeta_de_credito'].widget.attrs.update({'id': 'targeta'})
        self.fields['fecha_de_vencimiento'].widget.attrs.update({'id': 'fecha'})
        self.fields['codigo_de_seguridad'].widget.attrs.update({'id': 'cs'})
        
        
class updateUser(UserChangeForm):
    
    class Meta:
        model = useru 
        fields =["nombre","apellido","telefono","comuna","direccion"]

    def __init__(self, *args , **kwargs ):
        super().__init__(*args, **kwargs)
        self.helper= FormHelper()
        self.helper.form_method="post"
        self.helper.form_class="needs-validation"
        self.helper.attrs={"novalidate":""}
        self.helper.layout=Layout(
           Field("nombre",id="nombre"), 
           Field("apellido",id="apellido"), 
           Div(
                Div(
                    PrependedText('telefono', '+56', active=True , id="fono"),
                    css_class='input-group'
                ,id="fono2"),
                css_class='form-group'
            ),
           Field("comuna",id="comuna"), 
           Field("direccion",id="direc") 
        )
        # Elimina los campos de contraseña ya que no se necesitan para actualizar el perfil
        if 'password' in self.fields:
            del self.fields['password']
class upPassUser(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'needs-validation'
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Field('old_password', id='old_password'),
            Field('new_password1', id='contraseña'),
            Field('new_password2', id='repetirContraseña')
        )
  

class ItemCarritoForm(forms.ModelForm):
    class Meta:
        model = ItemCarrito
        fields = ['cantidad']


