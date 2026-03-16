from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    ESTADOS = [
        ("Borrador", "Borrador"),
        ("En revisión", "En revisión"),
        ("Aprobado", "Aprobado"),
        ("Rechazado", "Rechazado"),
        ("Archivado", "Archivado"),
    ]

    nombre = models.CharField(max_length=255)
    sector = models.CharField(max_length=150)
    problema = models.TextField()
    objetivo_general = models.TextField()
    poblacion_objetivo = models.CharField(max_length=255)
    presupuesto = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="Borrador")
    observaciones = models.TextField(blank=True)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-creado_en"]
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.nombre