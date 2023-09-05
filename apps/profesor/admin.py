from django.contrib import admin
from apps.profesor.models import Profesor, Tipo_Documento

# Register your models here.
admin.site.register(Tipo_Documento)
admin.site.register(Profesor)