from django.db.models import Count, Q
from django.shortcuts import render

from apps.projects.models import Project, ProjectReview, ProjectAttachment


def home(request):
    total_proyectos = Project.objects.count()

    proyectos_borrador = Project.objects.filter(estado="Borrador").count()
    proyectos_revision = Project.objects.filter(estado="En revisión").count()
    proyectos_aprobados = Project.objects.filter(estado="Aprobado").count()
    proyectos_rechazados = Project.objects.filter(estado="Rechazado").count()
    proyectos_archivados = Project.objects.filter(estado="Archivado").count()

    proyectos_urbanos = Project.objects.filter(
        Q(comuna__isnull=False) | Q(barrio__isnull=False)
    ).count()

    proyectos_rurales = Project.objects.filter(
        Q(corregimiento__isnull=False) | Q(vereda__isnull=False)
    ).count()

    sectores = (
        Project.objects.values("sector")
        .annotate(total=Count("id"))
        .order_by("-total", "sector")[:10]
    )

    total_reviews = ProjectReview.objects.count()
    total_attachments = ProjectAttachment.objects.count()

    estados_chart = [
        {"label": "Borrador", "value": proyectos_borrador},
        {"label": "En revisión", "value": proyectos_revision},
        {"label": "Aprobado", "value": proyectos_aprobados},
        {"label": "Rechazado", "value": proyectos_rechazados},
        {"label": "Archivado", "value": proyectos_archivados},
    ]

    territorial_chart = [
        {"label": "Urbanos", "value": proyectos_urbanos},
        {"label": "Rurales", "value": proyectos_rurales},
    ]

    context = {
        "total_proyectos": total_proyectos,
        "proyectos_borrador": proyectos_borrador,
        "proyectos_revision": proyectos_revision,
        "proyectos_aprobados": proyectos_aprobados,
        "proyectos_rechazados": proyectos_rechazados,
        "proyectos_archivados": proyectos_archivados,
        "proyectos_urbanos": proyectos_urbanos,
        "proyectos_rurales": proyectos_rurales,
        "sectores": sectores,
        "total_reviews": total_reviews,
        "total_attachments": total_attachments,
        "estados_chart": estados_chart,
        "territorial_chart": territorial_chart,
    }
    return render(request, "home.html", context)