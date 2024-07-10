from django.contrib import admin

from .models import Edificio, Salones, TipoSala
# Register your models here.

admin.site.register(Edificio)
admin.site.register(Salones)
admin.site.register(TipoSala)