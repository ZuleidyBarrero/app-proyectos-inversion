from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "nombre",
            "sector",
            "problema",
            "objetivo_general",
            "poblacion_objetivo",
            "comuna",
            "barrio",
            "corregimiento",
            "vereda",
            "presupuesto",
            "estado",
            "observaciones",
        ]
        widgets = {
            "problema": forms.Textarea(attrs={"rows": 4}),
            "objetivo_general": forms.Textarea(attrs={"rows": 4}),
            "observaciones": forms.Textarea(attrs={"rows": 4}),
        }