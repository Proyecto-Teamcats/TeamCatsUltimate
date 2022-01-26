from django import forms
from django.forms import ModelForm
from .models import Persona
from .models import Gato

class PersonaForm(forms.ModelForm):

    class Meta: 
        model= Persona
        fields = ['rut', 'pnombre', 'snombre', 'papellido', 'sapellido', 'edad', 'telefono', 'email', 'contrasena']
        labels ={
            'rut': 'Rut', 
            'pnombre': 'Primer nombre', 
            'snombre': 'Segundo nombre', 
            'papellido': 'Primer apellido', 
            'sapellido': 'Segundo apellido', 
            'edad': 'Edad',
            'telefono': 'Telefono', 
            'email': 'Email', 
            'contrasena': 'Contraseña',  
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'pnombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su primer nombre', 
                    'id': 'pnombre'
                }
            ), 
            'snombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su segundo nombre', 
                    'id': 'snombre'
                }
            ), 
            'papellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su primer apellido', 
                    'id': 'papellido'
                }
            ),
            'sapellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su segundo apellido', 
                    'id': 'sapellido'
                }
            ),
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su edad', 
                    'id': 'edad'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ejemplo +56951393925', 
                    'id': 'telefono'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ejemplo etzio@gmail.com', 
                    'id': 'email'
                }
            ),
            'contrasena': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su contraseña',
                    'type':'password',
                    'id': 'contrasena'
                }
            )
        }

class GatoForm(forms.ModelForm):

    class Meta: 
        model= Gato
        fields = ['id_chip', 'nombre', 'color', 'sexo', 'edad', 'Descripcion', 'raza', 'rut']
        labels ={
            'id_chip': 'ID de chip', 
            'nombre': 'Nombre de gatito', 
            'color': 'Color del gatito',
            'sexo': 'Genero del felino',  
            'edad': 'Edad del felino', 
            'Descripcion': 'Descripcion del cat',
            'raza': 'Raza del felino', 
            'rut': 'Rut del adoptador', 
        }
        widgets={
            'id_chip': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id de chip', 
                    'id': 'id_chip'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del gato', 
                    'id': 'nombre'
                }
            ), 
            'color': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su color', 
                    'id': 'color'
                }
            ), 
            'sexo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese genero del gato',  
                    'id': 'sexo'
                }
            ),
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese edad del gato', 
                    'id': 'edad'
                }
            ),
            'Descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese descripcion del gatito', 
                    'id': 'Descripcion'
                }
            ),
            'raza': forms.Select(
                attrs={
                    'class': 'form-control',  
                    'id': 'raza'
                }
            ),
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese rut del adoptador',
                    'id':'rut',
                }
            )

        }

 
    
     