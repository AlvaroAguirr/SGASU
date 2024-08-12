from django.contrib import admin

from .models import Building, Classroom, RoomType
# Register your models here.

class BuildingAdmin(admin.ModelAdmin):
    list_display = ['bg_name', 'bg_description']
admin.site.register(Building, BuildingAdmin)


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['cm_name', 'cm_furniture', 'cm_type', 'cm_description', 'cm_manager']
admin.site.register(Classroom, ClassroomAdmin)

class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['rm_type', 'rm_description']
admin.site.register(RoomType, RoomTypeAdmin)