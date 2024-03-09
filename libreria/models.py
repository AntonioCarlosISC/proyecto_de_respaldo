from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#Creacion del modelo personalizado para usuarios
class UsuarioPersonalizado(AbstractUser):
    OPCIONES_ROL = (
        ('sin_asignar', 'Sin asignar'),
        ('investigador', 'Investigador'),
        ('evaluador', 'Evaluador'),
        ('admin', 'Administrador'),
    )
    rol = models.CharField(verbose_name='rol',max_length=20,blank=True)

# Creación de los modelos que serán posteriormente migrados a la base de datos
class b1(models.Model):
    id = models.AutoField(primary_key=True) # <-- Aquí se genera la llave primaria que identificará la tabla con un ID
    nombre_especialidad = models.CharField(max_length=100, verbose_name="Nombre de la especialidad") # <-- A partir de aquí se declaran los campos de las tablas con sus respectivos atributos
    cedula_profesional = models.CharField(max_length=100, verbose_name="Cédula profesional", default= " ")
    fecha = models.TextField(verbose_name="Fecha de obtención", null=True)
    titulo = models.FileField(upload_to='media/archivos/',verbose_name="Titulo", null=True) #<-- Las rutas declaradas dentro de la función "upload_to" indican la ruta donde serán almacenados los archivos
    cedula = models.FileField( upload_to='media/archivos/',verbose_name="Cédula", null=True)
    carta_conacyt = models.FileField(upload_to='media/archivos/', verbose_name="Carta conacyt", null=True)
    
class b2(models.Model):
    idmae =	models.AutoField(primary_key=True)
    idinv = models.CharField(max_length=20, verbose_name="Id Investigador") 	
    nombre_maestría =models.CharField(max_length=100, verbose_name="Nombre de Maestría") 	 
    cedula_profesional = models.CharField(max_length=20, verbose_name="Cedula Profesional") 
    fecha_obtención	= models.TextField(verbose_name="Fecha Obtención de Grado",null=True )
    archivo_titulo =models.FileField( upload_to='media/archivos/',verbose_name="Archivo Titulo", null = True)	
    archivo_cedula =models.FileField( upload_to='media/archivos/',verbose_name="Archivo Cedula", null = True)
    archivo_carta_recono_conacyt=models.FileField( upload_to='media/archivos/',verbose_name="Archivo Carta", null = True)
    
class b3(models.Model):
    IdDoc =	models.AutoField(primary_key=True)
    idInv = models.IntegerField(verbose_name="Id Investigador") 	
    nombre_doctorado =models.CharField(max_length=100, verbose_name="Nombre del Doctorado") 	 
    cedula_profesional = models.CharField(max_length=20, verbose_name="Cedula Profesional") 
    fecha_obtención	= models.TextField(verbose_name="Fecha Obtención de Grado",null=True )
    archivo_titulo =models.FileField( upload_to='archivos/',verbose_name="Archivo Titulo", null = True)	
    archivo_cedula =models.FileField( upload_to='archivos/',verbose_name="Archivo Cedula", null = True)
    archivo_carta_recono_conacyt=models.FileField( upload_to='archivos/',verbose_name="Archivo Carta", null = True)
    

class b4(models.Model):
    IdMae =	models.AutoField(primary_key=True)
    idInv = models.IntegerField(verbose_name="Id Investigador")
    nombre_maestria =models.TextField(verbose_name="Nombre de la Especialidad")
    nombre_inst_edu =models.TextField(verbose_name="Nombre de la Institución Educativa")
    pais =models.TextField(verbose_name="País")
    fecha_obtención =models.TextField(verbose_name="Fecha de Obtención") 	 
    archivo_titulo= models.FileField( upload_to='archivos/',verbose_name="Archivo del Titulo")
    
class b5(models.Model):
    IdDoc =	models.AutoField(primary_key=True)
    idInv = models.IntegerField(verbose_name="Id Investigador")
    nombre_doctorado =models.TextField(max_length=100, verbose_name="Nombre de la Especialidad") 	 
    nombre_inst_edu =models.TextField(verbose_name="Nombre de la Institución Educativa")
    pais =models.TextField(verbose_name="País")
    fecha_obtención = models.TextField(verbose_name="Fecha de Obtención") 	 
    archivo_titulo= models.FileField( upload_to='archivos/',verbose_name="Archivo del Titulo")
    

class b6(models.Model):
    idEsp = models.AutoField(primary_key=True, verbose_name="Id de la Especialidad")
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    nom_especialidad = models.TextField(verbose_name="Nombre de la especialidad", null=False)
    ced_prof = models.TextField(verbose_name="Cedula Profesional", null=False)
    fech_obt = models.TextField(verbose_name="Fecha", null=False)
    arch_titulo = models.FileField(upload_to='archivos/', verbose_name="Archivo Titulo")
    arch_cedula = models.FileField(upload_to='archivos/', verbose_name="Archivo Cedula Profesional", null= True)
    
class b7(models.Model):
    IdMae = models.IntegerField(verbose_name="Id de Maestria",default='1')
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    nom_maes = models.TextField(verbose_name="Nombre de la Maestria")
    ced_prof = models.TextField(verbose_name="Cedula Profesional", null=False)
    fech_obt = models.TextField(verbose_name="Fecha", null=False)
    arch_titulo = models.FileField(upload_to='archivos/', verbose_name="Archivo Titulo")
    arch_cedula = models.FileField(upload_to='archivos/', verbose_name="Archivo Cedula Profesional", null= True)

class b8(models.Model):
    IdDoc = models.IntegerField(verbose_name="Id de Maestria",default='1')
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    nom_doc = models.TextField(verbose_name="Nombre del Doctorado")
    ced_prof = models.TextField(verbose_name="Cedula Profesional", null=False)
    fech_obt = models.TextField(verbose_name="Fecha", null=False)
    arch_titulo = models.FileField(upload_to='archivos/', verbose_name="Archivo Titulo")
    arch_cedula = models.FileField(upload_to='archivos/', verbose_name="Archivo Cedula Profesional", null= True)
    
class b9(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_dir_tes_lic = models.FileField(upload_to='archivos/', verbose_name = "Archivo de trabajo de dirección de trabajos de tesis de licenciatura de alumnos graduados y/o titulados.")
    
class b10(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_dir_tes_esp = models.FileField(upload_to='archivos/', verbose_name = "Archivo de trabajo de dirección de trabajos de tesis de especialidad médica de alumnos graduados y/o titulados.")
    
class b11(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_dir_tes_maes = models.FileField(upload_to='archivos/', verbose_name = "Archivo de trabajo de dirección de trabajos de tesis de maestría de doctorado de alumnos graduados y/o titulados.")
    
class b12(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_dir_tes_doc = models.FileField(upload_to='archivos/', verbose_name = "Archivo de trabajo de dirección de trabajos de tesis de alumnos graduados y/o titulados.")
    
class b13(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_ases_alum = models.FileField(upload_to='archivos/', verbose_name = "Archivo de trabajo de asesoría de alumno de licenciatura, especialidad, maestría o doctorado en estancia de investigación")
    
class b14(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    pon_cong_simp_inter = models.FileField(upload_to='archivos/', verbose_name = "Archivo de ponencias en congresos o simposios científicos internacionales")
    
class b15(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    pon_cong_simp_nac = models.FileField(upload_to='archivos/', verbose_name = "Archivo de ponencias en congresos o simposios científicos nacionales")
    
class b16(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    pres_cart_simp_inter = models.FileField(upload_to='archivos/', verbose_name = "Archivo de presentación de carteles en congresos o simposios científicos internacionales")
    
class b17(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    pres_cart_simp_nac = models.FileField(upload_to='archivos/', verbose_name = "Archivo de presentación de carteles en congresos o simposios científicos nacionales")   

class b18(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_estancia = models.FileField(upload_to='archivos/', verbose_name = "Archivo de Estancia de Investigación")
    
#class bb18(models.Model):
#    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
#    arch_estancia = models.FileField(upload_to='archivos/', verbose_name = "Archivo de Estancia de Investigación")
   
    
class b19(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_asignaturas = models.FileField(upload_to='archivos/', verbose_name = "Archivo de Asignaturas con créditos impartidas")
    
class b20(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_proyecto = models.FileField(upload_to='media/archivos/', verbose_name = "Archivo de registro del proyecto en la institución")
    
class b21(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_pub_art_rev = models.FileField(upload_to='media/archivos/', verbose_name = "Archivo publicación de artículo en revista no arbitrada de divulgación científica o tecnológica")
    
class b22(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_part_event = models.FileField(upload_to='media/archivos/', verbose_name = "Archivo departicipación en eventos de divulgación científica")
    
class b23(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_ev_trab_inv = models.FileField(upload_to='media/archivos/', verbose_name = "Archivo de evaluación de trabajos de Investigación o Proyectos")
 
    
class aa1(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_libro = models.FileField(upload_to='archivos/', verbose_name = "Archivo de libro cientifico con Arbitraje")


class a1(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_libro = models.FileField(upload_to='archivos/', verbose_name = "Archivo de libro cientifico con Arbitraje")
    
class a2(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_patente = models.FileField(upload_to='archivos/', verbose_name = "Archivo de Solicitud de Patente")

class a3(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_tit_patente = models.FileField(upload_to='archivos/', verbose_name = "Archivo de obtención del título de Derechos de Patente")
    
class a4(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_tram_obtentor = models.FileField(upload_to='archivos/', verbose_name = "Archivo de trámite de solicitud de derecho de obtentor")
    
class a5(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_dere_obtentor = models.FileField(upload_to='archivos/', verbose_name = "Archivo obtención de derecho de obtentor")
    
class a6(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_soft_autor = models.FileField(upload_to='archivos/', verbose_name = "Archivo desarrollo de software con derechos de autor")
    

class a7(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_art_rev_indx = models.FileField(upload_to='archivos/', verbose_name = "Archivo publicación de artículo o nota científica en revista indexada")


class a8(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_art_rev_arb = models.FileField(upload_to='archivos/', verbose_name = "Archivo publicación de artículo científico o nota científica en revista arbitrada.")

class a9(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_libr_cien_arb = models.FileField(upload_to='archivos/', verbose_name = "Autoría o Coautoría de capítulo de libro científico con arbitraje.")

class a10(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_carta_impl = models.FileField(upload_to='archivos/', verbose_name = "Implementación tecnológica.")
    
class a11(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_art_div_cien = models.FileField(upload_to='archivos/', verbose_name = "Archivo publicación de artículo o nota científica en revista arbitrada de divulgación científica obtecnológica.")
    
    
class a12(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_proy_inv_cien = models.FileField(upload_to='archivos/', verbose_name = "Archivo participación en proyectos de investigación científica, desarrollo tecnológico e innovación con financiamiento externo obtenido mediante convocatoria.")
    
class a13(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_inv_sni = models.FileField(upload_to='archivos/', verbose_name = "Archivo investigador perteneciente al SNI.")
    
class a14(models.Model):
    idInv = models.IntegerField(verbose_name="Id del Investigador",default='1')
    arch_edit_comp_coor = models.FileField(upload_to='archivos/', verbose_name = "Archivo de editor, compilador o coordinador de libro colectivo")
    
    
    def __str__(self):
        fila = "Documentos: " + self.documentos
        return fila
    
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

