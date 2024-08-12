from django.db import models

from solicitante.models import Applicant
from salas.models import Classroom
from horario.models import Schedule

# Create your models here.
class Request(models.Model):
    applicant_name = models.ForeignKey(Applicant, on_delete=models.CASCADE, verbose_name="Nombre solicitante")
    classroom_name = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING, verbose_name="Sala")
    rt_horario=models.OneToOneField(
        Schedule,
        on_delete=models.CASCADE,
        null=False,blank=False,default=1)


    
    def __str__(self):
        return f"{ self.applicant_name } { self.classroom_name } "
    
    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'