from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class RoomType(models.Model):
    rm_type = models.CharField(verbose_name="Tipo", max_length=100)
    rm_description = models.CharField(verbose_name="Descripción", max_length=150)

    def __str__(self):
        return f"{ self.rm_type } { self.rm_description }"

    class Meta:
        verbose_name = "Tipo de sala"
        verbose_name_plural = "Tipos de sala"

class Building(models.Model):
    bg_name = models.CharField(verbose_name="Nombre", max_length=15)
    bg_description = models.CharField(verbose_name="Descripción", max_length=50)

    def __str__(self):
        return f"{ self.bg_name } { self.bg_description }"
    
    class Meta:
        verbose_name = "Edificio"
        verbose_name_plural = "Edificios"

class Classroom(models.Model):
    cm_name = models.CharField(verbose_name="Nombre", max_length=15)
    cm_furniture = models.CharField(verbose_name="Moviliario", max_length=15)
    cm_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, verbose_name="Tipo de sala")
    cm_description = models.CharField(verbose_name="Descripción", max_length=150)
    cm_manager = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Administrador")

    def __str__(self):
        return f"{ self.cm_name }"
    
    class Meta:
        verbose_name = "Salón"
        verbose_name_plural = "Salones"




# class Horario(models.Model):
#     fecha = models.DateField
#     horas = models.IntegerField(max_length=1)

