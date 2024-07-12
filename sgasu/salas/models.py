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
    furniture = models.CharField(verbose_name="Moviliario", max_length=15)
    cm_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, verbose_name="Tipo de sala")
    cm_description = models.CharField(verbose_name="Descripción", max_length=150)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Administrador")

    def __str__(self):
        return f"{ self.cm_name } { self.furniture } { self.cm_type } { self.cm_description } { self.manager }"
    
    class Meta:
        verbose_name = "Salón"
        verbose_name_plural = "Salones"

# class Encargado(models.Model):
#     correo = models.CharField(max_length=30)
#     nombre = models.CharField(max_length=30)
#     telefono = models.IntegerField(max_length=10)
#     id_encargado = models.BigAutoField(primary_key=True)

# class Solicitante(models.Model):
#     motivo = models.CharField(max_length=30)
#     nombre = models.CharField(max_length=30)
#     matricula = models.CharField(max_length=30)

# class Horario(models.Model):
#     fecha = models.DateField
#     horas = models.IntegerField(max_length=1)

# class Peticion(models.Model):
#     recursos = models.CharField(max_length=30)

