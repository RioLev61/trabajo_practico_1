from django.db import models
from django.utils.text import slugify

# Create your models here.

'''class Contacto(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    email = models.EmailField(max_length=150,verbose_name='email')
    asunto = models.CharField(max_length=50,verbose_name='Asunto')
    mensaje = models.TextField(verbose_name='Mensaje')'''

class Categoria(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre

    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()

class Usuario(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    username = models.CharField(max_length=20,verbose_name='Nombre de Usuario')
    email = models.EmailField(max_length=150,verbose_name='email')
    password = models.CharField(max_length=20,verbose_name='Password')

    def __str__(self):
        return f"{self.username} - {self.nombre} {self.apellido}"
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    
    class Meta():
        verbose_name_plural = 'Usuarios'

class Posteo(models.Model):
    titulo = models.CharField(max_length=50,verbose_name='Titulo')
    resumen = models.CharField(max_length=250,verbose_name='Resumen')
    articulo = models.TextField(verbose_name='Articulo')
    imagenpos = models.ImageField(upload_to='#',verbose_name='ImagenPos')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True,verbose_name='Fecha')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    def delete(self,using=None,keep_parents=False):
        self.imagenpos.storage.delete(self.imagenpos.name) #borrado fisico
        super().delete()

class Proyectos(models.Model):
    nombrep = models.CharField(max_length=50,verbose_name='NombreP')
    imagenp = models.ImageField(upload_to='#',verbose_name='ImagenP')
    website = models.URLField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Comentarios(models.Model):
    nombrec = models.CharField(max_length=50,verbose_name='NombreC')
    comentarios = models.CharField(max_length=250,verbose_name='Comentarios')
    email = models.EmailField(max_length=150,verbose_name='email')
    fechac = models.DateField(auto_now=True,verbose_name='FechaC')
    post = models.ForeignKey(Posteo, on_delete=models.CASCADE)
