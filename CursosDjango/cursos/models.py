from django.db import models
from ckeditor.fields import RichTextField


class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    instructor = models.CharField(max_length=100)
    duracion_horas = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    cupo_maximo = models.PositiveSmallIntegerField()
    imagen = models.ImageField(upload_to='cursos_imagenes/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Actividad(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave de Actividad")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    descripcion = RichTextField(verbose_name="Descripción de la Actividad")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return f"Actividad de {self.curso.nombre} - {self.fecha_creacion.strftime('%Y-%m-%d')}"