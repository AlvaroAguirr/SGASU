from django.contrib import admin

from .models import Applicant

# Register your models here.

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['at_name', 'at_reason', 'at_school_enrollment']
    list_filter = ['at_name']

admin.site.register(Applicant, ApplicantAdmin)