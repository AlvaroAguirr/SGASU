from django.contrib import admin
from .models import Request

# Register your models here.
class RequestAdmin(admin.ModelAdmin):
    list_display = ['reason', 'name', 'school_enrollment', 'date']
    list_filter = ['date']

admin.site.register(Request, RequestAdmin)
