from django.contrib import admin

# Register your models here.
from .models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display=['se_day','se_start_time','se_end_time','se_classroom']
admin.site.register(Schedule,ScheduleAdmin)
