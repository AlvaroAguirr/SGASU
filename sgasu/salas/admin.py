from django.contrib import admin

from .models import Edificio, Salon, TipoSala
# Register your models here.

admin.site.register(Edificio)
admin.site.register(Salon)
admin.site.register(TipoSala)