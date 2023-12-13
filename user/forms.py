from django import forms
from .models import *

#Formulario de Creacion de Usuario en base al Modelo Usuario personalizado
class FormularioUsuarioNuevo(forms.ModelForm):
    password1 = forms.CharField(label= "Contraseña", widget= forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese su contraseña',
            'id':'password1',
            'required':'required',
        }
    ))

    password2 = forms.CharField(label= "Confirmar Contraseña", widget= forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('rut', 'nombre', 'apellido', 'email')
        widgets = {
            'rut': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Rut (con punto y guión)',    
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre',    
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Apellido',    
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Correo Electronico',    
                }
            )
        }
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2
    
    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
        