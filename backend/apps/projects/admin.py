from django.contrib import admin
from .models import Barrio, Comuna, Corregimiento, Project, Vereda


@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)


@admin.register(Corregimiento)
class CorregimientoAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)


@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "comuna")
    search_fields = ("nombre",)
    list_filter = ("comuna",)


@admin.register(Vereda)
class VeredaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "corregimiento")
    search_fields = ("nombre",)
    list_filter = ("corregimiento",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "sector",
        "estado",
        "comuna",
        "barrio",
        "corregimiento",
        "vereda",
        "creado_por",
        "creado_en",
    )
    search_fields = ("nombre", "sector", "poblacion_objetivo")
    list_filter = ("estado", "sector", "comuna", "corregimiento", "creado_en")