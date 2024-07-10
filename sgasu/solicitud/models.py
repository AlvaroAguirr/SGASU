from datetime import date
from django.db import models


# Create your models here.
class Request(models.Model):
    reason = models.CharField(verbose_name="Motivo", max_length=30)
    name = models.CharField(verbose_name="Nombre",max_length=30)
    school_enrollment= models.CharField(verbose_name="Matricula",max_length=30)
    date = models.DateTimeField(verbose_name= "Fecha")
    
    def __str__(self):
        return f"{ self.reason } { self.name } { self.school_enrollment } { self.date }"
    
    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'