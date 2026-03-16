from django.contrib import admin
from .models import (
    Barrio,
    Comuna,
    Corregimiento,
    Project,
    ProjectAttachment,
    ProjectStatusHistory,
    Vereda,
)


@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Corregimiento)
class CorregimientoAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "comuna")
    search_fields = ("nombre",)
    list_filter = ("comuna",)
    ordering = ("nombre",)


@admin.register(Vereda)
class VeredaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "corregimiento")
    search_fields = ("nombre",)
    list_filter = ("corregimiento",)
    ordering = ("nombre",)


class ProjectAttachmentInline(admin.TabularInline):
    model = ProjectAttachment
    extra = 1


class ProjectStatusHistoryInline(admin.TabularInline):
    model = ProjectStatusHistory
    extra = 0
    readonly_fields = ("estado_anterior", "estado_nuevo", "cambiado_por", "cambiado_en", "observacion")
    can_delete = False


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
    ordering = ("-creado_en",)
    inlines = [ProjectAttachmentInline, ProjectStatusHistoryInline]


@admin.register(ProjectAttachment)
class ProjectAttachmentAdmin(admin.ModelAdmin):
    list_display = ("project", "descripcion", "cargado_por", "cargado_en")
    search_fields = ("descripcion", "project__nombre")
    list_filter = ("cargado_en",)
    ordering = ("-cargado_en",)


@admin.register(ProjectStatusHistory)
class ProjectStatusHistoryAdmin(admin.ModelAdmin):
    list_display = ("project", "estado_anterior", "estado_nuevo", "cambiado_por", "cambiado_en")
    search_fields = ("project__nombre", "estado_anterior", "estado_nuevo", "observacion")
    list_filter = ("estado_nuevo", "cambiado_en")
    ordering = ("-cambiado_en",)