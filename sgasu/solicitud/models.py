from django.db import models

from solicitante.models import Applicant
from salas.models import Classroom

# Create your models here.
class Request(models.Model):
    fk_name = models.ForeignKey(Applicant, on_delete=models.CASCADE, verbose_name="Nombre solicitante")
    fk_classroom = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING, verbose_name="Sala")
    date = models.DateTimeField(verbose_name= "Fecha")
    
    def __str__(self):
        return f"{ self.fk_name } { self.fk_classroom } { self.date }"
    
    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'