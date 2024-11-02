from django import forms
from .models import Vendedor, Cliente, Deportivo, Registro_Compra, Rol, Usuario
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

# Formulario Rol 
class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre']

# Formulario usuario
class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'rol', 'password1', 'password2']
        exclude = ['createAt']

#Formulario para edición basico de el usuario
class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'rol']
        exclude = ['createAt']

#Formulario Vendedor    
class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre','apellidos','anos_trabajo']

class ClienteForm(forms.ModelForm):
    vendedor = forms.ModelChoiceField(queryset = Vendedor.objects.all(), empty_label = "Seleccione un Vendedor")
    class Meta:
        model = Cliente
        fields = ['nombre','direccion', 'telefono','vendedor']
        

class DeportivoForm(forms.ModelForm):
    class Meta:
       model = Deportivo
       fields = ['modelo','marca','precio','kilometraje','caballos_fuerza','imagen']
       labels={
           'modelo':'Modelo',
           'marca':'Marca',
           'precio':'Precio',
           'kilometraje':'kilometraje',
           'caballos_fuerza':'Caballos de Fuerza',
           'imagen':'Imagen del Auto',
       }
       widgets={
           'modelo':forms.TextInput(
               attrs={
                   'class':'form-control',
                   'placeholder':'Modelo'
               }
           ),
           'marca':forms.TextInput(
               attrs={
                   'class':'form-control',
                   'placeholder':'Marca'
               }
           ),
           'precio':forms.NumberInput(
               attrs={
                   'class':'form-control',
                   'placeholder':'Precio'
               }
           ),
           'kilometraje':forms.NumberInput(
               attrs={
                   'class':'form-control',
                   'placeholder':'Kilometraje'
               }
           ),
           'caballos_fuerza':forms.NumberInput(
               attrs={
                   'class':'form-control',
                   'placeholder':'Caballos de Fuerza'
               }
           ),
           'imagen':forms.FileInput(
               attrs={
                   'class':'form-control',
                   'placeholder':'Imagen del Auto'
               }
           )
          
           
       }
    
class CompraForm(forms.ModelForm):
    class Meta:
       model = Registro_Compra
       fields = ['deportivo','cliente','monto']
       exclude = ['createAt']
    
    
            
               
       
   


# FORMULARIO de Cambio de Contraseña
class ClientePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label = "Contraseña actual",
        widget = forms.PasswordInput(), 
        required = True
    )
    new_password1 = forms.CharField(
        label = "Nueva contraseña",
        widget = forms.PasswordInput(),
        required = True
    )
    new_password2 = forms.CharField(
        label = "Confirmar nueva contraseña",
        widget = forms.PasswordInput(),
        required = True
    )       

          