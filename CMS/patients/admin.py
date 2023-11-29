from django.contrib import admin
from .models import patients,treatment



admin.site.register(patients)
admin.site.register(treatment)
admin.site.site_header='clinicure admin'
