from django.db import models

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
