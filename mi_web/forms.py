from typing import Any
from django import forms
from .models import producto , Tarjeta , ItemCarrito , Boleta ,Bloqueo ,Desbloqueo
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm ,UserChangeForm ,PasswordChangeForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout , Submit , Div ,Field ,HTML
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



class BoletaForm(forms.ModelForm):
    class Meta:
        model = Boleta
        fields = ['metodoDePago', 'telefono2', 'comuna2', 'direccion2', 'rut_receptor', 'nombre_receptor']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['metodoDePago'].queryset = Tarjeta.objects.filter(uusuario=user)
        
        # Cambiar la etiqueta del campo
        self.fields['metodoDePago'].label = "Método de Pago"
        
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "needs-validation"
        self.helper.attrs = {"novalidate": ""}
        
        # Configurar el layout del formulario
        self.helper.layout = Layout(
            HTML('<h3>Datos de pago</h3>'),  # Título personalizado
            Field("metodoDePago", id="metodoDePago"),
            HTML('<h3>datos de direccion y metodo de contacto</h3>'),  # Título personalizado
            Field("comuna2", id="comuna"),
            Field("direccion2", id="direc"),
            Field("telefono2", id="fono"),
            HTML('<h3>Datos del Receptor</h3>'),  # Título personalizado
            Field("rut_receptor", id="Rut"),
            Field("nombre_receptor", id="nombre"),
            Submit('submit', 'Pagar', css_class='btn btn-primary')  # Botón personalizado
            
            
        )
        
        # Agregar atributos a los otros campos
        self.fields['telefono2'].widget.attrs.update({'id': 'fono'})
        self.fields['comuna2'].widget.attrs.update({'id': 'comuna'})
        self.fields['direccion2'].widget.attrs.update({'id': 'direc'})
        self.fields['rut_receptor'].widget.attrs.update({'id': 'Rut'})
        self.fields['nombre_receptor'].widget.attrs.update({'id': 'nombre'})
        
        
class UsuarioFilterForm(forms.Form):
    nombre = forms.CharField(required=False, label='Nombre')
    apellido = forms.CharField(required=False, label='Apellido')
    es_baneado = forms.BooleanField(required=False, label='Es baneado', initial=False)
    
    
class BloqueoForm(forms.ModelForm):
    class Meta:
        model = Bloqueo
        fields = ['razon']
        
class DesbloqueoForm(forms.ModelForm):
    class Meta:
        model = Desbloqueo
        fields = ['razon']
        