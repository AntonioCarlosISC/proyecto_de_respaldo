from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static



urlpatterns = [
    path('',views.home, name='home'),
    path('evaluador',views.evaluador,name='evaluador'),
    
    path('evaluacion_a1', views.evaluacion_a1, name='evaluacion_a1'),
    path('evaluacion_a2', views.evaluacion_a2, name='evaluacion_a2'),
    path('evaluacion_a3', views.evaluacion_a3, name='evaluacion_a3'),
    path('evaluacion_a4', views.evaluacion_a4, name='evaluacion_a4'),
    path('evaluacion_a5', views.evaluacion_a5, name='evaluacion_a5'),
    path('evaluacion_a6', views.evaluacion_a6, name='evaluacion_a6'),
    path('evaluacion_a7', views.evaluacion_a7, name='evaluacion_a7'),
    path('evaluacion_a8', views.evaluacion_a8, name='evaluacion_a8'),
    path('evaluacion_a9', views.evaluacion_a9, name='evaluacion_a9'),
    path('evaluacion_a10', views.evaluacion_a10, name='evaluacion_a10'),
    path('evaluacion_a11', views.evaluacion_a11, name='evaluacion_a11'),
    path('evaluacion_a12', views.evaluacion_a12, name='evaluacion_a12'),
    path('evaluacion_a13', views.evaluacion_a13, name='evaluacion_a13'),
    path('evaluacion_a14', views.evaluacion_a14, name='evaluacion_a14'),
    path('evaluacion_b1', views.evaluacion_b1, name='evaluacion_b1'),
    path('evaluacion_b2', views.evaluacion_b2, name='evaluacion_b2'),
    path('evaluacion_b3', views.evaluacion_b3, name='evaluacion_b3'),
    path('evaluacion_b4', views.evaluacion_b4, name='evaluacion_b4'),
    path('evaluacion_b5', views.evaluacion_b5, name='evaluacion_b5'),
    path('evaluacion_b6', views.evaluacion_b6, name='evaluacion_b6'),
    path('evaluacion_b7', views.evaluacion_b7, name='evaluacion_b7'),
    path('evaluacion_b8', views.evaluacion_b8, name='evaluacion_b8'),
    path('evaluacion_b9', views.evaluacion_b9, name='evaluacion_b9'),
    path('evaluacion_b10', views.evaluacion_b10, name='evaluacion_b10'),
    path('evaluacion_b11', views.evaluacion_b11, name='evaluacion_b11'),
    path('evaluacion_b12', views.evaluacion_b12, name='evaluacion_b12'),
    path('evaluacion_b13', views.evaluacion_b13, name='evaluacion_b13'),
    path('evaluacion_b14', views.evaluacion_b14, name='evaluacion_b14'),
    path('evaluacion_b15', views.evaluacion_b15, name='evaluacion_b15'),
    path('evaluacion_b16', views.evaluacion_b16, name='evaluacion_b16'),
    path('evaluacion_b17', views.evaluacion_b17, name='evaluacion_b17'),
    path('evaluacion_b18', views.evaluacion_b18, name='evaluacion_b18'),
    path('evaluacion_b19', views.evaluacion_b19, name='evaluacion_b19'),
    path('evaluacion_b20', views.evaluacion_b20, name='evaluacion_b20'),
    path('evaluacion_b21', views.evaluacion_b21, name='evaluacion_b21'),
    path('evaluacion_b22', views.evaluacion_b22, name='evaluacion_b22'),
    path('evaluacion_b23', views.evaluacion_b23, name='evaluacion_b23'),

    path('redirigiendo',views.redirigir_usuario,name='redirigiendo'),
    path('contacto',views.nosotros, name='contacto'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('regresar',views.regresar, name='regresar'),
    path('registro',views.registro, name='registro'),
    path('acerca',views.acerca, name='acerca'),
    path('i_ses',views.i_ses, name='i_ses'),
    path('salir',views.salir, name='salir'),
    path('profile',views.profile, name='profile'),
    path('carousel',views.carousel, name='carousel'),
    path('ciencia',views.ciencia, name='ciencia'),
    path('superacion',views.superacion, name='superacion'),
    path('productividad',views.productividad, name='productividad'),
    path('participacion',views.participacion, name='participacion'),
    path('sni',views.sni, name='sni'),
    path('superacionAca',views.superacionAca, name='superacionAca'),
    path('rh',views.rh, name='rh'),
    path('ponencias',views.ponencias, name='ponencias'),
    path('otros',views.otros, name='otros'),
    path('cat_a1',views.cat_a1, name='cat_a1'),
    path('cat_a2',views.cat_a2, name='cat_a2'),
    path('cat_a3',views.cat_a3, name='cat_a3'),
    path('cat_a4',views.cat_a4, name='cat_a4'),
    path('cat_a5',views.cat_a5, name='cat_a5'),
    path('cat_a6',views.cat_a6, name='cat_a6'),
    path('cat_a7',views.cat_a7, name='cat_a7'),
    path('cat_a8',views.cat_a8, name='cat_a8'),
    path('cat_a9',views.cat_a9, name='cat_a9'),
    path('cat_a10',views.cat_a10, name='cat_a10'),
    path('cat_a11',views.cat_a11, name='cat_a11'),
    path('cat_a12',views.cat_a12, name='cat_a12'),
    path('cat_a13',views.cat_a13, name='cat_a13'),
    path('cat_a14',views.cat_a14, name='cat_a14'),
    path('cat_b1',views.cat_b1, name='cat_b1'),
    path('cat_b2',views.cat_b2, name='cat_b2'),
    path('cat_b3',views.cat_b3, name='cat_b3'),
    path('cat_b4',views.cat_b4, name='cat_b4'),
    path('cat_b5',views.cat_b5, name='cat_b5'),
    path('cat_b6',views.cat_b6, name='cat_b6'),
    path('cat_b7',views.cat_b7, name='cat_b7'),
    path('cat_b8',views.cat_b8, name='cat_b8'),
    path('cat_b9',views.cat_b9, name='cat_b9'),
    path('cat_b10',views.cat_b10, name='cat_b10'),
    path('cat_b11',views.cat_b11, name='cat_b11'),
    path('cat_b12',views.cat_b12, name='cat_b12'),
    path('cat_b13',views.cat_b13, name='cat_b13'),
    path('cat_b14',views.cat_b14, name='cat_b14'),
    path('cat_b15',views.cat_b15, name='cat_b15'),
    path('cat_b16',views.cat_b16, name='cat_b16'),
    path('cat_b17',views.cat_b17, name='cat_b17'),
    path('cat_b18',views.cat_b18, name='cat_b18'),
    path('cat_b19',views.cat_b19, name='cat_b19'),
    path('cat_b20',views.cat_b20, name='cat_b20'),
    path('cat_b21',views.cat_b21, name='cat_b21'),
    path('cat_b22',views.cat_b22, name='cat_b22'),
    path('cat_b23',views.cat_b23, name='cat_b23'),
    path('crear_a1',views.crear_a1, name='crear_a1'),
    path('crear_a2',views.crear_a2, name='crear_a2'),
    path('crear_a3',views.crear_a3, name='crear_a3'),
    path('crear_a4',views.crear_a4, name='crear_a4'),
    path('crear_a5',views.crear_a5, name='crear_a5'),
    path('crear_a6',views.crear_a6, name='crear_a6'),
    path('crear_a7',views.crear_a7, name='crear_a7'),
    path('crear_a8',views.crear_a8, name='crear_a8'),
    path('crear_a9',views.crear_a9, name='crear_a9'),
    path('crear_a10',views.crear_a10, name='crear_a10'),
    path('crear_a11',views.crear_a11, name='crear_a11'),
    path('crear_a12',views.crear_a12, name='crear_a12'),
    path('crear_a13',views.crear_a13, name='crear_a13'),
    path('crear_a14',views.crear_a14, name='crear_a14'),
    path('crear',views.crear, name='crear'),
    path('crear_b1',views.crear_b1, name='crear_b1'),
    path('crear_b2',views.crear_b2, name='crear_b2'),
    path('crear_b3',views.crear_b3, name='crear_b3'),
    path('crear_b4',views.crear_b4, name='crear_b4'),
    path('crear_b5',views.crear_b5, name='crear_b5'),
    path('crear_b7',views.crear_b7, name='crear_b7'),
    path('crear_b8',views.crear_b8, name='crear_b8'),
    path('crear_b9',views.crear_b9, name='crear_b9'),
    path('crear_b10',views.crear_b10, name='crear_b10'),
    path('crear_b11',views.crear_b11, name='crear_b11'),
    path('crear_b12',views.crear_b12, name='crear_b12'),
    path('crear_b13',views.crear_b13, name='crear_b13'),
    path('crear_b14',views.crear_b14, name='crear_b14'),
    path('crear_b15',views.crear_b15, name='crear_b15'),
    path('crear_b16',views.crear_b16, name='crear_b16'),
    path('crear_b17',views.crear_b17, name='crear_b17'),
    path('crear_b18',views.crear_b18, name='crear_b18'),
    path('crear_b19',views.crear_b19, name='crear_b19'),
    path('crear_b20',views.crear_b20, name='crear_b20'),
    path('crear_b21',views.crear_b21, name='crear_b21'),
    path('crear_b22',views.crear_b22, name='crear_b22'),
    path('crear_b23',views.crear_b23, name='crear_b23'),
    path('form_a1',views.form_a1, name='form_a1'),
    path('form_a2',views.form_a2, name='form_a2'),
    path('form_a3',views.form_a3, name='form_a3'),
    path('form_a4',views.form_a4, name='form_a4'),
    path('form_a5',views.form_a5, name='form_a5'),
    path('form_a6',views.form_a6, name='form_a6'),
    path('form_a7',views.form_a7, name='form_a7'),
    path('form_a8',views.form_a8, name='form_a8'),
    path('form_a9',views.form_a9, name='form_a9'),
    path('form_a10',views.form_a10, name='form_a10'),
    path('form_a11',views.form_a11, name='form_a11'),
    path('form_a12',views.form_a12, name='form_a12'),
    path('form_a13',views.form_a13, name='form_a13'),
    path('form_a14',views.form_a14, name='form_a14'),
    path('form',views.form, name='form'),
    path('form_b1',views.form_b1, name='form_b1'),
    path('form_b2',views.form_b2, name='form_b2'),
    path('form_b3',views.form_b3, name='form_b3'),
    path('form_b4',views.form_b4, name='form_b4'),
    path('form_b5',views.form_b5, name='form_b5'),
    path('form_b7',views.form_b7, name='form_b7'),
    path('form_b8',views.form_b8, name='form_b8'),
    path('form_b9',views.form_b9, name='form_b9'),
    path('form_b10',views.form_b10, name='form_b10'),
    path('form_b11',views.form_b11, name='form_b11'),
    path('form_b12',views.form_b12, name='form_b12'),
    path('form_b13',views.form_b13, name='form_b13'),
    path('form_b14',views.form_b14, name='form_b14'),
    path('form_b15',views.form_b15, name='form_b15'),
    path('form_b16',views.form_b16, name='form_b16'),
    path('form_b17',views.form_b17, name='form_b17'),
    path('form_b18',views.form_b18, name='form_b18'),
    path('form_b19',views.form_b19, name='form_b19'),
    path('form_b20',views.form_b20, name='form_b20'),
    path('form_b21',views.form_b21, name='form_b21'),
    path('form_b22',views.form_b22, name='form_b22'),
    path('form_b23',views.form_b23, name='form_b23'),
   
    
    path('editar_a1 <int:idInv>',views.editar_a1, name='editar_a1'),
    path('editar_a2 <int:idInv>',views.editar_a2, name='editar_a2'),
    path('editar_a3 <int:idInv>',views.editar_a3, name='editar_a3'),
    path('editar_a4 <int:idInv>',views.editar_a4, name='editar_a4'),
    path('editar_a5 <int:idInv>',views.editar_a5, name='editar_a5'),
    path('editar_a6 <int:idInv>',views.editar_a6, name='editar_a6'),
    path('editar_a7 <int:idInv>',views.editar_a7, name='editar_a7'),
    path('editar_a8 <int:idInv>',views.editar_a8, name='editar_a8'), 
    path('editar_a9 <int:idInv>',views.editar_a9, name='editar_a9'),
    path('editar_a10 <int:idInv>',views.editar_a10, name='editar_a10'),
    path('editar_a11 <int:idInv>',views.editar_a11, name='editar_a11'),
    path('editar_a12 <int:idInv>',views.editar_a12, name='editar_a12'),  
    path('editar_a13 <int:idInv>',views.editar_a13, name='editar_a13'),
    path('editar_a14 <int:idInv>',views.editar_a14, name='editar_a14'),
              
    
    path('editar <int:idInv>',views.editar, name='editar'),
    path('editar_b1 <int:id>',views.editar_b1, name='editar_b1'),
    path('editar_b2 <int:idInv>',views.editar_b2, name='editar_b2'),
    path('editar_b3 <int:idInv>',views.editar_b3, name='editar_b3'),
    path('editar_b4 <int:idInv>',views.editar_b4, name='editar_b4'),
    path('editar_b5 <int:idInv>',views.editar_b5, name='editar_b5'),
    path('editar_b7 <int:idInv>',views.editar_b7, name='editar_b7'),
    path('editar_b8 <int:idInv>',views.editar_b8, name='editar_b8'),
    path('editar_b9 <int:idInv>',views.editar_b9, name='editar_b9'),
    path('editar_b10 <int:idInv>',views.editar_b10, name='editar_b10'),
    path('editar_b11 <int:idInv>',views.editar_b11, name='editar_b11'),
    path('editar_b12 <int:idInv>',views.editar_b12, name='editar_b12'),
    path('editar_b13 <int:idInv>',views.editar_b13, name='editar_b13'),
    path('editar_b14 <int:idInv>',views.editar_b14, name='editar_b14'),
    path('editar_b15 <int:idInv>',views.editar_b15, name='editar_b15'),
    path('editar_b16 <int:idInv>',views.editar_b16, name='editar_b16'),
    path('editar_b17 <int:idInv>',views.editar_b17, name='editar_b17'),
    
    path('editar_b18 <int:idInv>',views.editar_b18, name='editar_b18'),
    path('editar_b19 <int:idInv>',views.editar_b19, name='editar_b19'),
    path('editar_b20 <int:idInv>',views.editar_b20, name='editar_b20'),
    path('editar_b21 <int:idInv>',views.editar_b21, name='editar_b21'),
    path('editar_b22 <int:idInv>',views.editar_b22, name='editar_b22'),
    path('editar_b23 <int:idInv>',views.editar_b23, name='editar_b23'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
