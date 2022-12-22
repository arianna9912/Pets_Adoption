from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pets(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    estatura = models.CharField(max_length=20)
    raza= models.CharField(max_length=30)
    adoptado=models.BooleanField()

    class Meta:
        verbose_name = 'Pets'
        ordering = ['id']


class Adoption(models.Model):
    pets = models.ForeignKey(Pets, on_delete=models.CASCADE)
    nombre_mascota=models.CharField(max_length=20)
    direccion_persona=models.CharField(max_length=50)
    fecha = models.DateTimeField()
    descripcion_mascota=models.CharField(max_length=150)
    nombre_dueno=models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Adoption'
        ordering = ['id']
