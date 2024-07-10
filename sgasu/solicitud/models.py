from datetime import date
from django.db import models


# Create your models here.
class Solicitudes(models.Model):
    motivo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    matricula = models.CharField(max_length=30)
    fecha = models.DateTimeField(verbose_name= "Fecha")
    
