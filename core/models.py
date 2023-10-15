from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    rubro = models.CharField(max_length=15)
    matricula = models.CharField(max_length=15)
    dni = models.IntegerField(max_length=15)
    edad = models.IntegerField(max_length=15, default=0)
    domicilio = models.CharField(max_length=20, null=True)