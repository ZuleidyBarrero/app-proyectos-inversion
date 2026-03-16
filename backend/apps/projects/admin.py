from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("nombre", "sector", "estado", "creado_por", "creado_en")
    search_fields = ("nombre", "sector", "poblacion_objetivo")
    list_filter = ("estado", "sector", "creado_en")