from django.db import models


from salas.models import Classroom

# Create your models here.
class Schedule (models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Lunes'),
        ('Tuesday', 'Martes'),
        ('Wednesday', 'Miércoles'),
        ('Thursday', 'Jueves'),
        ('Friday', 'Viernes'),
        ('Saturday', 'Sábado'),
        ('Sunday', 'Domingo'),
    ]


    se_day = models.CharField(
        max_length=9,  
        choices=DAYS_OF_WEEK,  
        verbose_name='Día'
    )
    se_start_time=models.TimeField(verbose_name="horario inicio")
    se_end_time=models.TimeField(verbose_name="hora de finalizacion")
    se_classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE, related_name="horario_de_salon", default=2)



    def __str__(self):
        return f"{self.se_day} {self.se_start_time} {self.se_end_time} {self.se_classroom}"
    
    class Meta:
        verbose_name = "Horario de salon"
        verbose_name_plural = "Horarios de salones" 