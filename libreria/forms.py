from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm #<-- Importamos la biblioteca forms de Django
from .models import (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, 
                     b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, 
                     b15, b16, b17, b18, b19, b20, b21, b22, b23,UsuarioPersonalizado) #<--- Importamos los modelos a utilizar


modelos = (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14,         #<--- Se conetienen en esta tupla el nombre de los modelos a usarse.
                     b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, 
                     b15, b16, b17, b18, b19, b20, b21, b22, b23)                     

formularios = {} #<--- Diccionario que contendrá las clases

for modelo in modelos: #<--- Se crea una iteración recorriendo cada nombre de modelo asignado en la tupla modelos.
    formulario_clase = type(f'{modelo.__name__}Form',(ModelForm,),{ # <--- Creando una nueva clase para el modelo iterado
        'Meta': type('Meta', (),{'model': modelo, 'fields': '__all__'})
    })

    formularios[modelo.__name__] = formulario_clase #<--- En esta lista se contienen todos las clases creadas

# Creación de los formularios
a1Form =  formularios['a1']
a2Form =  formularios['a2']
a3Form =  formularios['a3']
a3Form =  formularios['a3']
a4Form =  formularios['a4']
a5Form =  formularios['a5']
a6Form =  formularios['a6']
a7Form =  formularios['a7']
a8Form =  formularios['a8']
a9Form =  formularios['a9']
a10Form = formularios['a10']
a11Form = formularios['a11']
a12Form = formularios['a12']
a13Form = formularios['a13']
a14Form = formularios['a14']


b1Form =  formularios['b1']
b2Form =  formularios['b2']
b3Form =  formularios['b3']
b3Form =  formularios['b3']
b4Form =  formularios['b4']
b5Form =  formularios['b5']
b6Form =  formularios['b6']
b7Form =  formularios['b7']
b8Form =  formularios['b8']
b9Form =  formularios['b9']
b10Form = formularios['b10']
b11Form = formularios['b11']
b12Form = formularios['b12']
b13Form = formularios['b13']
b14Form = formularios['b14']
b15Form = formularios['b15']
b16Form = formularios['b16']
b17Form = formularios['b17']
b18Form = formularios['b18']
b19Form = formularios['b19']
b20Form = formularios['b20']
b21Form = formularios['b21']
b22Form = formularios['b22']
b23Form = formularios['b23']

User = UsuarioPersonalizado

class FormularioPersonalizadoUsuario(UserCreationForm):
    OPCIONES_ROL = (
        ('investigador', 'Investigador'),
        ('evaluador', 'Evaluador'),
        ('admin', 'Administrador'),
    )
    rol = forms.ChoiceField(choices=OPCIONES_ROL, required=False, label='Rol')
    class Meta:
        model = User
        fields = ("username","email","rol","password1","password2",)
        