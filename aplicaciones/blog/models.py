
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la categoria', max_length=100, null= False, blank=False)
    estado = models.BooleanField('Categoría Activada/Categoría no Activada', default= True)
    fecha_creacion = models.DateField('Fecha Creación',auto_now = False, auto_now_add=True)

    class meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id= models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField( 'Nombre del Autor' ,max_length=255, blank=True, null=False)
    apellidos = models.CharField( 'Apellidos del Autor' ,max_length=255, blank=True, null=False)
    imagen = models.ImageField(default='img/profile2.png')
    facebook = models.URLField( 'Facebook', blank=True, null=True)
    github = models.URLField( 'Github', blank=True, null=True)
    twitter = models.URLField( 'Twitter', blank=True, null=True)
    web = models.URLField( 'Web', blank=True, null=True)
    correo = models.EmailField( 'Correo Electrónico', blank=True, null=False)
    estado = models.BooleanField( 'Autor Activo/Autor no Activo', default= True)
    fecha_creacion = models.DateField('Fecha Creación',auto_now = False, auto_now_add=True)
    class meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombres)

    def create_autor(sender, instance,created ,**kwargs):
        if created:
            Autor.objects.create(user=instance)

    post_save.connect(create_autor, sender=User)




# Clase Posteo

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=90, blank=False, null= False)
    slug = models.CharField(max_length=100, blank=False, null= False)
    descripcion = models.CharField(max_length=110, blank=False, null= False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=255, blank=False, null= False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = models.DateTimeField('Fecha de Creación',auto_now= False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo


class Project(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    imagen = models.URLField(max_length=255, blank=False, null= False)
    url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.titulo