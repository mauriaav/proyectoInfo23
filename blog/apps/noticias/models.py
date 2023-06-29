from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    resumen = models.TextField()
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to = 'noticias')

    categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE)

    def __str__(self):
        return self.titulo
        