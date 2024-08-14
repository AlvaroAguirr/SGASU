from django.db import models

# Create your models here.

class Applicant(models.Model):
    at_name = models.CharField(verbose_name="Nombre",max_length=30)
    at_reason = models.CharField(verbose_name="Motivo", max_length=30)
    at_school_enrollment= models.CharField(verbose_name="Matricula",max_length=30)

    def __str__(self):
        return f" { self.at_name }"
    
    class Meta:
        verbose_name = 'Solicitante'
        verbose_name_plural = 'Solicitantes'