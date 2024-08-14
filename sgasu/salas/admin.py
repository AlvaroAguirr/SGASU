from django.contrib import admin

from .models import Building, Classroom, RoomType
from horario.models import Schedule

class ScheduleInline(admin.TabularInline):  # Puedes usar admin.StackedInline si prefieres un diseño diferente
    model = Schedule
    extra = 1  # Cuántos formularios en blanco deseas agregar por defecto
    fields = ['se_day', 'se_start_time', 'se_end_time','se_classroom']

# Register your models here.

class BuildingAdmin(admin.ModelAdmin):
    list_display = ['bg_name', 'bg_description']
admin.site.register(Building, BuildingAdmin)


class ClassroomAdmin(admin.ModelAdmin):
    
    list_display = ['cm_name', 'cm_furniture', 'cm_type', 'cm_description', 'cm_manager']
    filter_horizontal = ('horarios',)
admin.site.register(Classroom, ClassroomAdmin)

class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['rm_type', 'rm_description']
admin.site.register(RoomType, RoomTypeAdmin)



