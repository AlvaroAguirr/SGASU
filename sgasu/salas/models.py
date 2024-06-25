from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TipoSala(models.Model):
    tipo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)

class Edificio(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=50)

class Salon(models.Model):
    nombre = models.CharField(max_length=15)
    moviliario = models.CharField(max_length=15)
    tipo = models.ForeignKey(TipoSala, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150)
    encargado = models.ForeignKey(User, on_delete=models.CASCADE)

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

