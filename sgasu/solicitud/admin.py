from django.contrib import admin
from .models import Request

# Register your models here.
class RequestAdmin(admin.ModelAdmin):
    list_display = ['applicant_name', 'classroom_name', 'date']


admin.site.register(Request, RequestAdmin)