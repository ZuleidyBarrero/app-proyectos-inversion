from django.db import models
from django.contrib.auth.models import User


class Comuna(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Comuna"
        verbose_name_plural = "Comunas"

    def __str__(self):
        return self.nombre


class Corregimiento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Corregimiento"
        verbose_name_plural = "Corregimientos"

    def __str__(self):
        return self.nombre


class Barrio(models.Model):
    nombre = models.CharField(max_length=150)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name="barrios")

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Barrio"
        verbose_name_plural = "Barrios"
        unique_together = ("nombre", "comuna")

    def __str__(self):
        return f"{self.nombre} - {self.comuna.nombre}"


class Vereda(models.Model):
    nombre = models.CharField(max_length=150)
    corregimiento = models.ForeignKey(Corregimiento, on_delete=models.CASCADE, related_name="veredas")

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Vereda"
        verbose_name_plural = "Veredas"
        unique_together = ("nombre", "corregimiento")

    def __str__(self):
        return f"{self.nombre} - {self.corregimiento.nombre}"


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

    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True, blank=True)
    barrio = models.ForeignKey(Barrio, on_delete=models.SET_NULL, null=True, blank=True)
    corregimiento = models.ForeignKey(Corregimiento, on_delete=models.SET_NULL, null=True, blank=True)
    vereda = models.ForeignKey(Vereda, on_delete=models.SET_NULL, null=True, blank=True)

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


class ProjectAttachment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="attachments")
    archivo = models.FileField(upload_to="projects/attachments/")
    descripcion = models.CharField(max_length=255, blank=True)
    cargado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    cargado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-cargado_en"]
        verbose_name = "Anexo de proyecto"
        verbose_name_plural = "Anexos de proyecto"

    def __str__(self):
        return self.descripcion or self.archivo.name
class ProjectStatusHistory(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="status_history")
    estado_anterior = models.CharField(max_length=20, blank=True)
    estado_nuevo = models.CharField(max_length=20)
    cambiado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    cambiado_en = models.DateTimeField(auto_now_add=True)
    observacion = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-cambiado_en"]
        verbose_name = "Historial de estado"
        verbose_name_plural = "Historial de estados"

    def __str__(self):
        return f"{self.project.nombre}: {self.estado_anterior} -> {self.estado_nuevo}"
class ProjectReview(models.Model):
    TIPOS = [
        ("Tecnica", "Técnica"),
        ("Juridica", "Jurídica"),
        ("Financiera", "Financiera"),
        ("General", "General"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="reviews")
    tipo = models.CharField(max_length=20, choices=TIPOS, default="General")
    observacion = models.TextField()
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado_en"]
        verbose_name = "Observación de revisión"
        verbose_name_plural = "Observaciones de revisión"

    def __str__(self):
        return f"{self.project.nombre} - {self.tipo}"