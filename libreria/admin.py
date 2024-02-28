from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (aa1,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,UsuarioPersonalizado)

#Definicion de una tupla con todos los nombres de los modelos a registrar
modelos = (aa1,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,
        b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,
        b17,b18,b19,b20,b21,b22,b23)

# Register your models here.

#Se registran los modelos mediante un for each (recorriendo cada elemento de la tupla modelos)
for modelo in modelos:
    admin.site.register(modelo)
    
admin.site.register(UsuarioPersonalizado)