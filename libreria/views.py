from django.shortcuts import render,redirect
from email import message
from multiprocessing import context
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .forms import *
from .models import (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18, b19, b20,b21,b22,b23)

# Aquí se crean todas las vistas a utilizarse
def generar_vista(plantilla):
    def vista(request):
        return render(request,plantilla)
    return vista

# Generación de las vistas usando una función de fabrica (Solo se implementa para las rutas que no necesitan de más parametros y su funcionalidad es exactamente la misma)
# Aqui se organizan las vistas de la carpeta página
home = generar_vista('paginas/home.html')
regresar = generar_vista('paginas/regresar.html')
nosotros = generar_vista('paginas/contacto.html')
contacto = generar_vista('paginas/contacto.html')
acerca = generar_vista('paginas/acerca.html')
carousel = generar_vista('paginas/carousel.html')
#Aquí se organizan las vistas de la carpeta menu
ciencia = generar_vista('menu/ciencia.html')
superacion = generar_vista('menu/superacion.html')
productividad = generar_vista('menu/productividad.html')
participacion = generar_vista('menu/participacion.html')
sni = generar_vista('menu/sni.html')
superacionAca = generar_vista('menu/superacionAca.html')
rh = generar_vista('menu/rh.html')
ponencias = generar_vista('menu/ponencias.html')
otros = generar_vista('menu/otros.html')


#Aqui se organizan las vistas de las carpeta usuario
profile = generar_vista('usuario/profile.html')

#Funcion de fabrica para agregar los cat_
def generar_cat(modelo):
    def cat(request):
        objetos = modelo.objects.all()
        pagina = f'menu/cat_{modelo.__name__.lower()}.html'
        contexto = {f'cat_{modelo.__name__.lower()}': objetos}
        return render(request, pagina, contexto)
    return cat

#Se agregan los cat_a usando la funcion de fabrica previamente creada
cat_a1 = generar_cat(a1)
cat_a2 = generar_cat(a2)
cat_a3 = generar_cat(a3)
cat_a4 = generar_cat(a4)
cat_a5 = generar_cat(a5)
cat_a6 = generar_cat(a6)
cat_a7 = generar_cat(a7)
cat_a8 = generar_cat(a8)
cat_a9 = generar_cat(a9)
cat_a10 = generar_cat(a10)
cat_a11 = generar_cat(a11)
cat_a12 = generar_cat(a12)
cat_a13 = generar_cat(a13)
cat_a14 = generar_cat(a14)

cat_b1 = generar_cat(b1)
cat_b2 = generar_cat(b2)
cat_b3 = generar_cat(b3)
cat_b4 = generar_cat(b4)
cat_b5 = generar_cat(b5)
cat_b6 = generar_cat(b6)
cat_b7 = generar_cat(b7)
cat_b8 = generar_cat(b8)
cat_b9 = generar_cat(b9)
cat_b10 = generar_cat(b10)
cat_b11 = generar_cat(b11)
cat_b12 = generar_cat(b12)
cat_b13 = generar_cat(b13)
cat_b14 = generar_cat(b14)
cat_b15 = generar_cat(b15)
cat_b16 = generar_cat(b16)
cat_b17 = generar_cat(b17)
cat_b18 = generar_cat(b18)
cat_b19 = generar_cat(b19)
cat_b20 = generar_cat(b20)
cat_b21 = generar_cat(b21)
cat_b22 = generar_cat(b22)
cat_b23 = generar_cat(b23)



#Funcion de fabrica para los form_
def gen_form(plantilla):
    def form_(request):
        return render(request,plantilla)
    return form_

form_numeros = {}

#Se agregan los form mediante la funcion de fabrica
form_a1 = gen_form('menu/form_a1.html')
form_a2 = gen_form('menu/form_a2.html')
form_a3 = gen_form('menu/form_a3.html')
form_a4 = gen_form('menu/form_a4.html')
form_a5 = gen_form('menu/form_a5.html')
form_a6 = gen_form('menu/form_a6.html')
form_a7 = gen_form('menu/form_a7.html')
form_a8 = gen_form('menu/form_a8.html')
form_a9 = gen_form('menu/form_a9.html')
form_a10 = gen_form('menu/form_a10.html')
form_a11 = gen_form('menu/form_a11.html')
form_a12 = gen_form('menu/form_a12.html')
form_a13 = gen_form('menu/form_a13.html')
form_a14 = gen_form('menu/form_a14.html')

form = gen_form('menu/form.html')

form_b1 = gen_form('menu/form_a1.html')
form_b2 = gen_form('menu/form_a2.html')
form_b3 = gen_form('menu/form_a3.html')
form_b4 = gen_form('menu/form_a4.html')
form_b5 = gen_form('menu/form_a5.html')
form_b6 = gen_form('menu/form_a6.html')
form_b7 = gen_form('menu/form_a7.html')
form_b8 = gen_form('menu/form_a8.html')
form_b9 = gen_form('menu/form_a9.html')
form_b10 = gen_form('menu/form_a10.html')
form_b11 = gen_form('menu/form_a11.html')
form_b12 = gen_form('menu/form_a12.html')
form_b13 = gen_form('menu/form_a13.html')
form_b14 = gen_form('menu/form_a14.html')
form_b15 = gen_form('menu/form_a15.html')
form_b16 = gen_form('menu/form_a16.html')
form_b17 = gen_form('menu/form_a17.html')
form_b18 = gen_form('menu/form_a18.html')
form_b19 = gen_form('menu/form_a19.html')
form_b20 = gen_form('menu/form_a20.html')
form_b21 = gen_form('menu/form_a21.html')
form_b22 = gen_form('menu/form_a22.html')
form_b23 = gen_form('menu/form_a23.html')

#Aquí van las funciones que deben definirse de manera especifica
@login_required
def redirigir_usuario(request):
    # Obtiene el rol del usuario logueado
    rol_usuario = request.user.rol

    # Redirige al panel de evaluador si el usuario es un evaluador
    if rol_usuario == 'evaluador':
        return redirect('evaluador')
    # Redirige al panel de investigador si el usuario es un investigador
    elif rol_usuario == 'investigador':
        return redirect('home')
    # Redirige a la página de inicio si el usuario tiene cualquier otro rol
    else:
        return redirect('home')


def evaluador(request):
    cat_a1 = a1.objects.all()
    return render(request,'paginas/panel_evaluador.html',{'cat_a1':cat_a1})


#Funcion de fabrica para la vista evaluador
def generar_vista_evaluador(*modelos):
    def vista_evaluador(request):
        contexto = {}
        for modelo in modelos:
            objetos = modelo.objects.all()
            contexto[f'{modelo.__name__.lower()}s'] = objetos
        # Asume que tienes una plantilla genérica para mostrar todas las categorías
        pagina = 'paginas/panel_evaluador.html'
        return render(request, pagina, contexto)
    return vista_evaluador

# Usando la nueva función para generar una vista que incluye todos los modelos
vista_evaluador = generar_vista_evaluador(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18, b19, b20,b21,b22,b23)


def salir(request):
    logout(request)
    return redirect('/')

def registro(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == 'POST':
        form = FormularioPersonalizadoUsuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('redirigiendo')
        else:
            return render(request,'usuario/registro.html', {'form': form})
    else:
        print("Se ejecuta esta parte")
        form = FormularioPersonalizadoUsuario()
        return render(request,'usuario/registro.html',{'form':form})
    
def i_ses(request):
    if request.user.is_authenticated:
        return render(request, 'paginas/home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('redirigiendo') #profile
        else:
            msg = '¡Error al Iniciar Sesion!'
            form = AuthenticationForm(request.POST)
            return render(request, 'usuario/i_ses.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'usuario/i_ses.html', {'form': form})


def crear_a1(request):

    formulario_a1 = a1Form(request.POST or None, request.FILES or None)
    if formulario_a1.is_valid():
        formulario_a1.save()
        return redirect('cat_a1')
    return render(request, 'menu/crear_a1.html',{'formulario_a1': formulario_a1})

def crear_a2(request):

    formulario_a2 = a2Form(request.POST or None, request.FILES or None)
    if formulario_a2.is_valid():
        formulario_a2.save()
        return redirect('cat_a2')
    return render(request, 'menu/crear_a2.html',{'formulario_a2': formulario_a2})

def crear_a3(request):
    formulario_a3 = a3Form(request.POST or None, request.FILES or None)
    if formulario_a3.is_valid():
        formulario_a3.save()
        return redirect('cat_a3')
    return render(request, 'menu/crear_a3.html',{'formulario_a3': formulario_a3})

def crear_a4(request):
    formulario_a4 = a4Form(request.POST or None, request.FILES or None)
    if formulario_a4.is_valid():
        formulario_a4.save()
        return redirect('cat_a4')
    return render(request, 'menu/crear_a4.html',{'formulario_a4': formulario_a4})

def crear_a5(request):
    formulario_a5 = a5Form(request.POST or None, request.FILES or None)
    if formulario_a5.is_valid():
        formulario_a5.save()
        return redirect('cat_a5')
    return render(request, 'menu/crear_a5.html',{'formulario_a5': formulario_a5})

def crear_a6(request):
    formulario_a6 = a6Form(request.POST or None, request.FILES or None)
    if formulario_a6.is_valid():
        formulario_a6.save()
        return redirect('cat_a6')
    return render(request, 'menu/crear_a6.html',{'formulario_a6': formulario_a6})

def crear_a7(request):
    formulario_a7 = a7Form(request.POST or None, request.FILES or None)
    if formulario_a7.is_valid():
        formulario_a7.save()
        return redirect('cat_a7')
    return render(request, 'menu/crear_a7.html',{'formulario_a7': formulario_a7})

def crear_a8(request):
    formulario_a8 = a8Form(request.POST or None, request.FILES or None)
    if formulario_a8.is_valid():
        formulario_a8.save()
        return redirect('cat_a8')
    return render(request, 'menu/crear_a8.html',{'formulario_a8': formulario_a8})

def crear_a9(request):
    formulario_a9 = a9Form(request.POST or None, request.FILES or None)
    if formulario_a9.is_valid():
        formulario_a9.save()
        return redirect('cat_a9')
    return render(request, 'menu/crear_a9.html',{'formulario_a9': formulario_a9})

def crear_a10(request):
    formulario_a10 = a10Form(request.POST or None, request.FILES or None)
    if formulario_a10.is_valid():
        formulario_a10.save()
        return redirect('cat_a10')
    return render(request, 'menu/crear_a10.html',{'formulario_a10': formulario_a10})

def crear_a11(request):
    formulario_a11 = a11Form(request.POST or None, request.FILES or None)
    if formulario_a11.is_valid():
        formulario_a11.save()
        return redirect('cat_a11')
    return render(request, 'menu/crear_a11.html',{'formulario_a11': formulario_a11})

def crear_a12(request):
    formulario_a12 = a12Form(request.POST or None, request.FILES or None)
    if formulario_a12.is_valid():
        formulario_a12.save()
        return redirect('cat_a12')
    return render(request, 'menu/crear_a12.html',{'formulario_a12': formulario_a12})

def crear_a13(request):
    formulario_a13 = a13Form(request.POST or None, request.FILES or None)
    if formulario_a13.is_valid():
        formulario_a13.save()
        return redirect('cat_a13')
    return render(request, 'menu/crear_a13.html',{'formulario_a13': formulario_a13})

def crear_a14(request):
    formulario_a14 = a14Form(request.POST or None, request.FILES or None)
    if formulario_a14.is_valid():
        formulario_a14.save()
        return redirect('cat_a14')
    return render(request, 'menu/crear_a14.html',{'formulario_a14': formulario_a14})


def crear(request):
    formulario = b6Form(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('cat_b6')
    return render(request, 'menu/crear.html',{'formulario': formulario})

def crear_b1(request):
    formulario_b1 = b1Form(request.POST or None, request.FILES or None)
    if formulario_b1.is_valid():
        formulario_b1.save()
        return redirect('cat_b1')
    return render(request, 'menu/crear_b1.html',{'formulario_b1': formulario_b1})

def crear_b2(request):
    formulario_b2 = b2Form(request.POST or None, request.FILES or None)
    if formulario_b2.is_valid():
        formulario_b2.save()
        return redirect('cat_b2')
    return render(request, 'menu/crear_b2.html',{'formulario_b2': formulario_b2})

def crear_b3(request):
    formulario_b3 = b3Form(request.POST or None, request.FILES or None)
    if formulario_b3.is_valid():
        formulario_b3.save()
        return redirect('cat_b3')
    return render(request, 'menu/crear_b3.html',{'formulario_b3': formulario_b3})

def crear_b4(request):
    formulario_b4 = b4Form(request.POST or None, request.FILES or None)
    if formulario_b4.is_valid():
        formulario_b4.save()
        return redirect('cat_b4')
    return render(request, 'menu/crear_b4.html',{'formulario_b4': formulario_b4})

def crear_b5(request):
    formulario_b5 = b5Form(request.POST or None, request.FILES or None)
    if formulario_b5.is_valid():
        formulario_b5.save()
        return redirect('cat_b5')
    return render(request, 'menu/crear_b5.html',{'formulario_b5': formulario_b5})

def crear_b7(request):
    formulario_b7 = b7Form(request.POST or None, request.FILES or None)
    if formulario_b7.is_valid():
        formulario_b7.save()
        return redirect('cat_b7')
    return render(request, 'menu/crear_b7.html',{'formulario_b7': formulario_b7})

def crear_b8(request):
    formulario_b8 = b8Form(request.POST or None, request.FILES or None)
    if formulario_b8.is_valid():
        formulario_b8.save()
        return redirect('cat_b8')
    return render(request, 'menu/crear_b8.html',{'formulario_b8': formulario_b8})

def crear_b9(request):
    formulario_b9 = b9Form(request.POST or None, request.FILES or None)
    if formulario_b9.is_valid():
        formulario_b9.save()
        return redirect('cat_b9')
    return render(request, 'menu/crear_b9.html',{'formulario_b9': formulario_b9})

def crear_b10(request):
    formulario_b10 = b10Form(request.POST or None, request.FILES or None)
    if formulario_b10.is_valid():
        formulario_b10.save()
        return redirect('cat_b10')
    return render(request, 'menu/crear_b10.html',{'formulario_b10': formulario_b10})

def crear_b11(request):
    formulario_b11 = b11Form(request.POST or None, request.FILES or None)
    if formulario_b11.is_valid():
        formulario_b11.save()
        return redirect('cat_b11')
    return render(request, 'menu/crear_b11.html',{'formulario_b11': formulario_b11})

def crear_b12(request):
    formulario_b12 = b12Form(request.POST or None, request.FILES or None)
    if formulario_b12.is_valid():
        formulario_b12.save()
        return redirect('cat_b12')
    return render(request, 'menu/crear_b12.html',{'formulario_b12': formulario_b12})

def crear_b13(request):
    formulario_b13 = b13Form(request.POST or None, request.FILES or None)
    if formulario_b13.is_valid():
        formulario_b13.save()
        return redirect('cat_b13')
    return render(request, 'menu/crear_b13.html',{'formulario_b13': formulario_b13})

def crear_b14(request):
    formulario_b14 = b14Form(request.POST or None, request.FILES or None)
    if formulario_b14.is_valid():
        formulario_b14.save()
        return redirect('cat_b14')
    return render(request, 'menu/crear_b14.html',{'formulario_b14': formulario_b14})

def crear_b15(request):
    formulario_b15 = b15Form(request.POST or None, request.FILES or None)
    if formulario_b15.is_valid():
        formulario_b15.save()
        return redirect('cat_b15')
    return render(request, 'menu/crear_b15.html',{'formulario_b15': formulario_b15})

def crear_b16(request):
    formulario_b16 = b16Form(request.POST or None, request.FILES or None)
    if formulario_b16.is_valid():
        formulario_b16.save()
        return redirect('cat_b16')
    return render(request, 'menu/crear_b16.html',{'formulario_b16': formulario_b16})

def crear_b17(request):
    formulario_b17 = b17Form(request.POST or None, request.FILES or None)
    if formulario_b17.is_valid():
        formulario_b17.save()
        return redirect('cat_b17')
    return render(request, 'menu/crear_b17.html',{'formulario_b17': formulario_b17})


def crear_b18(request):
    formulario_b18 = b18Form(request.POST or None, request.FILES or None)
    if formulario_b18.is_valid():
        formulario_b18.save()
        return redirect('cat_b18')
    return render(request, 'menu/crear_b18.html',{'formulario_b18': formulario_b18})

def crear_b19(request):
    formulario_b19 = b19Form(request.POST or None, request.FILES or None)
    if formulario_b19.is_valid():
        formulario_b19.save()
        return redirect('cat_b19')
    return render(request, 'menu/crear_b19.html',{'formulario_b19': formulario_b19})

def crear_b20(request):
    formulario_b20 = b20Form(request.POST or None, request.FILES or None)
    if formulario_b20.is_valid():
        formulario_b20.save()
        return redirect('cat_b20')
    return render(request, 'menu/crear_b20.html',{'formulario_b20': formulario_b20})

def crear_b21(request):
    formulario_b21 = b21Form(request.POST or None, request.FILES or None)
    if formulario_b21.is_valid():
        formulario_b21.save()
        return redirect('cat_b21')
    return render(request, 'menu/crear_b21.html',{'formulario_b21': formulario_b21})

def crear_b22(request):
    formulario_b22 = b22Form(request.POST or None, request.FILES or None)
    if formulario_b22.is_valid():
        formulario_b22.save()
        return redirect('cat_b22')
    return render(request, 'menu/crear_b22.html',{'formulario_b22': formulario_b22})

def crear_b23(request):
    formulario_b23 = b23Form(request.POST or None, request.FILES or None)
    if formulario_b23.is_valid():
        formulario_b23.save()
        return redirect('cat_b23')
    return render(request, 'menu/crear_b23.html',{'formulario_b23': formulario_b23})

def editar_a1(request, idInv):
    documento_a1 = a1.objects.get(idInv=idInv)
    formulario_a1 = a1Form(request.POST or None, request.FILES or None, instance=documento_a1)
    if formulario_a1.is_valid() and request.POST:
        formulario_a1.save()
        return redirect('cat_a1')
    return render(request, 'menu/editar_a1.html', {'formulario_a1':formulario_a1})

def editar_a2(request, idInv):
    documento_a2 = a2.objects.get(idInv=idInv)
    formulario_a2 = a2Form(request.POST or None, request.FILES or None, instance=documento_a2)
    if formulario_a2.is_valid() and request.POST:
        formulario_a2.save()
        return redirect('cat_a2')
    return render(request, 'menu/editar_a2.html', {'formulario_a2':formulario_a2})

def editar_a3(request, idInv):
    documento_a3 = a3.objects.get(idInv=idInv)
    formulario_a3 = a3Form(request.POST or None, request.FILES or None, instance=documento_a3)
    if formulario_a3.is_valid() and request.POST:
        formulario_a3.save()
        return redirect('cat_a3')
    return render(request, 'menu/editar_a3.html', {'formulario_a3':formulario_a3})

def editar_a4(request, idInv):
    documento_a4 = a4.objects.get(idInv=idInv)
    formulario_a4 = a4Form(request.POST or None, request.FILES or None, instance=documento_a4)
    if formulario_a4.is_valid() and request.POST:
        formulario_a4.save()
        return redirect('cat_a4')
    return render(request, 'menu/editar_a4.html', {'formulario_a4':formulario_a4})

def editar_a5(request, idInv):
    documento_a5 = a5.objects.get(idInv=idInv)
    formulario_a5 = a5Form(request.POST or None, request.FILES or None, instance=documento_a5)
    if formulario_a5.is_valid() and request.POST:
        formulario_a5.save()
        return redirect('cat_a5')
    return render(request, 'menu/editar_a5.html', {'formulario_a5':formulario_a5})

def editar_a6(request, idInv):                  
    documento_a6 = a6.objects.get(idInv=idInv)
    formulario_a6 = a6Form(request.POST or None, request.FILES or None, instance=documento_a6)
    if formulario_a6.is_valid() and request.POST:
        formulario_a6.save()
        return redirect('cat_a6')
    return render(request, 'menu/editar_a6.html', {'formulario_a6':formulario_a6})

def editar_a7(request, idInv):
    documento_a7 = a7.objects.get(idInv=idInv)
    formulario_a7 = a7Form(request.POST or None, request.FILES or None, instance=documento_a7)
    if formulario_a7.is_valid() and request.POST:
        formulario_a7.save()
        return redirect('cat_a7')
    return render(request, 'menu/editar_a7.html', {'formulario_a7':formulario_a7})

def editar_a8(request, idInv):
    documento_a8 = a8.objects.get(idInv=idInv)
    formulario_a8 = a8Form(request.POST or None, request.FILES or None, instance=documento_a8)
    if formulario_a8.is_valid() and request.POST:
        formulario_a8.save()
        return redirect('cat_a8')
    return render(request, 'menu/editar_a8.html', {'formulario_a8':formulario_a8})

def editar_a9(request, idInv):
    documento_a9 = a9.objects.get(idInv=idInv)
    formulario_a9 = a9Form(request.POST or None, request.FILES or None, instance=documento_a9)
    if formulario_a9.is_valid() and request.POST:
        formulario_a9.save()
        return redirect('cat_a9')
    return render(request, 'menu/editar_a9.html', {'formulario_a9':formulario_a9})

def editar_a10(request, idInv):
    documento_a10 = a10.objects.get(idInv=idInv)
    formulario_a10 = a10Form(request.POST or None, request.FILES or None, instance=documento_a10)
    if formulario_a10.is_valid() and request.POST:
        formulario_a10.save()
        return redirect('cat_a10')
    return render(request, 'menu/editar_a10.html', {'formulario_a10':formulario_a10})

def editar_a11(request, idInv):
    documento_a11 = a11.objects.get(idInv=idInv)
    formulario_a11 = a11Form(request.POST or None, request.FILES or None, instance=documento_a11)
    if formulario_a11.is_valid() and request.POST:
        formulario_a11.save()
        return redirect('cat_a11')
    return render(request, 'menu/editar_a11.html', {'formulario_a11':formulario_a11})

def editar_a12(request, idInv):
    documento_a12 = a12.objects.get(idInv=idInv)
    formulario_a12 = a12Form(request.POST or None, request.FILES or None, instance=documento_a12)
    if formulario_a12.is_valid() and request.POST:
        formulario_a12.save()
        return redirect('cat_a12')
    return render(request, 'menu/editar_a12.html', {'formulario_a12':formulario_a12})

def editar_a13(request, idInv):
    documento_a13 = a13.objects.get(idInv=idInv)
    formulario_a13 = a13Form(request.POST or None, request.FILES or None, instance=documento_a13)
    if formulario_a13.is_valid() and request.POST:
        formulario_a13.save()
        return redirect('cat_a13')
    return render(request, 'menu/editar_a13.html', {'formulario_a13':formulario_a13})

def editar_a14(request, idInv):
    documento_a14 = a14.objects.get(idInv=idInv)
    formulario_a14 = a14Form(request.POST or None, request.FILES or None, instance=documento_a14)
    if formulario_a14.is_valid() and request.POST:
        formulario_a14.save()
        return redirect('cat_a14')
    return render(request, 'menu/editar_a14.html', {'formulario_a14':formulario_a14})

def editar_b1(request, id):
    documento_b1 = b1.objects.get(id=id)
    formulario_b1 = b1Form(request.POST or None, request.FILES or None, instance=documento_b1)
    if formulario_b1.is_valid() and request.POST:
        formulario_b1.save()
        return redirect('cat_b1')
    return render(request, 'menu/editar_b1.html', {'formulario_b1':formulario_b1})

def editar_b2(request, idInv):
    documento_b2 = b2.objects.get(idInv=idInv)
    formulario_b2 = b2Form(request.POST or None, request.FILES or None, instance=documento_b2)
    if formulario_b2.is_valid() and request.POST:
        formulario_b2.save()
        return redirect('cat_b2')
    return render(request, 'menu/editar_b2.html', {'formulario_b2':formulario_b2})

def editar_b3(request, idInv):
    documento_b3 = b3.objects.get(idInv=idInv)
    formulario_b3 = b3Form(request.POST or None, request.FILES or None, instance=documento_b3)
    if formulario_b3.is_valid() and request.POST:
        formulario_b3.save()
        return redirect('cat_b3')
    return render(request, 'menu/editar_b3.html', {'formulario_b3':formulario_b3})


def editar_b4(request, idInv):
    documento_b4 = b4.objects.get(idInv=idInv)
    formulario_b4 = b4Form(request.POST or None, request.FILES or None, instance=documento_b4)
    if formulario_b4.is_valid() and request.POST:
        formulario_b4.save()
        return redirect('cat_b4')
    return render(request, 'menu/editar_b4.html', {'formulario_b4':formulario_b4})

def editar_b5(request, idInv):
    documento_b5 = b5.objects.get(idInv=idInv)
    formulario_b5 = b5Form(request.POST or None, request.FILES or None, instance=documento_b5)
    if formulario_b5.is_valid() and request.POST:
        formulario_b5.save()
        return redirect('cat_b5')
    return render(request, 'menu/editar_b5.html', {'formulario_b5':formulario_b5})


def editar(request, idInv):
    documento = b6.objects.get(idInv=idInv)
    formulario = b6Form(request.POST or None, request.FILES or None, instance=documento)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('cat_b6')
    return render(request, 'menu/editar.html', {'formulario':formulario})


def editar_b7(request, idInv):
    documento_b7 = b7.objects.get(idInv=idInv)
    formulario_b7 = b7Form(request.POST or None, request.FILES or None, instance=documento_b7)
    if formulario_b7.is_valid() and request.POST:
        formulario_b7.save()
        return redirect('cat_b7')
    return render(request, 'menu/editar_b7.html', {'formulario_b7':formulario_b7})

def editar_b8(request, idInv):
    documento_b8 = b8.objects.get(idInv=idInv)
    formulario_b8 = b8Form(request.POST or None, request.FILES or None, instance=documento_b8)
    if formulario_b8.is_valid() and request.POST:
        formulario_b8.save()
        return redirect('cat_b8')
    return render(request, 'menu/editar_b8.html', {'formulario_b8':formulario_b8})

def editar_b9(request, idInv):
    documento_b9 = b9.objects.get(idInv=idInv)
    formulario_b9 = b9Form(request.POST or None, request.FILES or None, instance=documento_b9)
    if formulario_b9.is_valid() and request.POST:
        formulario_b9.save()
        return redirect('cat_b9')
    return render(request, 'menu/editar_b9.html', {'formulario_b9':formulario_b9})

def editar_b10(request, idInv):
    documento_b10 = b10.objects.get(idInv=idInv)
    formulario_b10 = b10Form(request.POST or None, request.FILES or None, instance=documento_b10)
    if formulario_b10.is_valid() and request.POST:
        formulario_b10.save()
        return redirect('cat_b10')
    return render(request, 'menu/editar_b10.html', {'formulario_b10':formulario_b10})

def editar_b11(request, idInv):
    documento_b11 = b11.objects.get(idInv=idInv)
    formulario_b11 = b11Form(request.POST or None, request.FILES or None, instance=documento_b11)
    if formulario_b11.is_valid() and request.POST:
        formulario_b11.save()
        return redirect('cat_b11')
    return render(request, 'menu/editar_b11.html', {'formulario_b11':formulario_b11})

def editar_b12(request, idInv):
    documento_b12 = b12.objects.get(idInv=idInv)
    formulario_b12 = b12Form(request.POST or None, request.FILES or None, instance=documento_b12)
    if formulario_b12.is_valid() and request.POST:
        formulario_b12.save()
        return redirect('cat_b12')
    return render(request, 'menu/editar_b12.html', {'formulario_b12':formulario_b12})

def editar_b13(request, idInv):
    documento_b13_list = b13.objects.filter(idInv=idInv)
    if documento_b13_list.exists():
        documento_b13 = documento_b13_list.first()
    else:
        # Manejar el caso en que no se encuentre ningún objeto b13
        pass

    formulario_b13 = b13Form(request.POST or None, request.FILES or None, instance=documento_b13)
    if formulario_b13.is_valid() and request.POST:
        formulario_b13.save()
        return redirect('cat_b13')
    return render(request, 'menu/editar_b13.html', {'formulario_b13':formulario_b13})

#def editar_b13(request, idInv):
#    documento_b13 = b13.objects.get(idInv=idInv)
#    formulario_b13 = b13Form(request.POST or None, request.FILES or None, instance=documento_b13)
#    if formulario_b13.is_valid() and request.POST:
#        formulario_b13.save()
#        return redirect('cat_b13')
#    return render(request, 'menu/editar_b13.html', {'formulario_b13':formulario_b13})

def editar_b14(request, idInv):
    documento_b14 = b14.objects.get(idInv=idInv)
    formulario_b14 = b14Form(request.POST or None, request.FILES or None, instance=documento_b14)
    if formulario_b14.is_valid() and request.POST:
        formulario_b14.save()
        return redirect('cat_b14')
    return render(request, 'menu/editar_b14.html', {'formulario_b14':formulario_b14})

def editar_b15(request, idInv):
    documento_b15 = b15.objects.get(idInv=idInv)
    formulario_b15 = b15Form(request.POST or None, request.FILES or None, instance=documento_b15)
    if formulario_b15.is_valid() and request.POST:
        formulario_b15.save()
        return redirect('cat_b15')
    return render(request, 'menu/editar_b15.html', {'formulario_b15':formulario_b15})

def editar_b16(request, idInv):
    documento_b16 = b16.objects.get(idInv=idInv)
    formulario_b16 = b16Form(request.POST or None, request.FILES or None, instance=documento_b16)
    if formulario_b16.is_valid() and request.POST:
        formulario_b16.save()
        return redirect('cat_b16')
    return render(request, 'menu/editar_b16.html', {'formulario_b16':formulario_b16})

def editar_b17(request, idInv):
    documento_b17 = b17.objects.get(idInv=idInv)
    formulario_b17 = b17Form(request.POST or None, request.FILES or None, instance=documento_b17)
    if formulario_b17.is_valid() and request.POST:
        formulario_b17.save()
        return redirect('cat_b17')
    return render(request, 'menu/editar_b17.html', {'formulario_b17':formulario_b17})

def editar_b18(request,idInv):
    documento_b18 = bb18.objects.get(idInv=idInv)
    formulario_b18 = b18Form(request.POST or None, request.FILES or None, instance=documento_b18)
    if formulario_b18.is_valid() and request.POST:
        formulario_b18.save()
        return redirect('cat_b18')
    return render(request, 'menu/editar_b18.html', {'formulario_b18':formulario_b18})

def editar_b19(request,idInv):
    documento_b19 = b19.objects.get(idInv=idInv)
    formulario_b19 = b19Form(request.POST or None, request.FILES or None, instance=documento_b19)
    if formulario_b19.is_valid() and request.POST:
        formulario_b19.save()
        return redirect('cat_b19')
    return render(request, 'menu/editar_b19.html', {'formulario_b19':formulario_b19})

def editar_b20(request,idInv):
    documento_b20 = b20.objects.get(idInv=idInv)
    formulario_b20 = b20Form(request.POST or None, request.FILES or None, instance=documento_b20)
    if formulario_b20.is_valid() and request.POST:
        formulario_b20.save()
        return redirect('cat_b20')
    return render(request, 'menu/editar_b20.html', {'formulario_b20':formulario_b20})

def editar_b21(request,idInv):
    documento_b21 = b21.objects.get(idInv=idInv)
    formulario_b21 = b21Form(request.POST or None, request.FILES or None, instance=documento_b21)
    if formulario_b21.is_valid() and request.POST:
        formulario_b21.save()
        return redirect('cat_b21')
    return render(request, 'menu/editar_b21.html', {'formulario_b21':formulario_b21})

def editar_b22(request,idInv):
    documento_b22 = b22.objects.get(idInv=idInv)
    formulario_b22 = b22Form(request.POST or None, request.FILES or None, instance=documento_b22)
    if formulario_b22.is_valid() and request.POST:
        formulario_b22.save()
        return redirect('cat_b22')
    return render(request, 'menu/editar_b22.html', {'formulario_b22':formulario_b22})

def editar_b23(request,idInv):
    documento_b23 = b23.objects.get(idInv=idInv)
    formulario_b23 = b23Form(request.POST or None, request.FILES or None, instance=documento_b23)
    if formulario_b23.is_valid() and request.POST:
        formulario_b23.save()
        return redirect('cat_b23')
    return render(request, 'menu/editar_b23.html', {'formulario_b23':formulario_b23})
