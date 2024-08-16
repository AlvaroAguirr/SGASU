from django.db import models
from django.core.exceptions import ValidationError


from solicitante.models import Applicant
from salas.models import Classroom
from horario.models import Schedule

from multiselectfield import MultiSelectField


import datetime
# Create your models here.
class Request(models.Model):
    extras=[
        ('microphones','micrófonos'),
        ('podium','estrado'),
        ('presidio','presidio'),
        ('proyector','projector')
    ]
    applicant_name = models.CharField(max_length=30,verbose_name="nombre_de_solicitante")
    rt_objetos=MultiSelectField(
        choices=extras,
        verbose_name="extras",blank=True,null=True)
    classroom_name = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING, verbose_name="Sala")
    rt_horario=models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        null=False,blank=False,default=1)
    request_time = models.TimeField(verbose_name="Hora de la solicitud",blank=True,default=datetime.time(0, 0))



    def __str__(self):
        return f"{ self.applicant_name } { self.classroom_name } "
    
    def clean(self):
        super().clean()
        if not (self.rt_horario.se_start_time <= self.request_time <= self.rt_horario.se_end_time):
            raise ValidationError(f"La hora {self.request_time} no está dentro del rango del horario {self.rt_horario}.")
        # Verifica si el horario ya está reservado



    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'