from django import forms
from .models import (
    Barrio,
    Comuna,
    Corregimiento,
    Project,
    ProjectAttachment,
    ProjectReview,
    Vereda,
)

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["comuna"].queryset = Comuna.objects.all().order_by("nombre")
        self.fields["corregimiento"].queryset = Corregimiento.objects.all().order_by("nombre")

        self.fields["barrio"].queryset = Barrio.objects.none()
        self.fields["vereda"].queryset = Vereda.objects.none()

        self.fields["comuna"].required = False
        self.fields["barrio"].required = False
        self.fields["corregimiento"].required = False
        self.fields["vereda"].required = False

        self.fields["comuna"].empty_label = "Seleccione una comuna"
        self.fields["barrio"].empty_label = "Seleccione un barrio"
        self.fields["corregimiento"].empty_label = "Seleccione un corregimiento"
        self.fields["vereda"].empty_label = "Seleccione una vereda"

        # Si viene POST, filtra barrios/veredas según lo seleccionado
        if "comuna" in self.data:
            try:
                comuna_id = int(self.data.get("comuna"))
                self.fields["barrio"].queryset = Barrio.objects.filter(comuna_id=comuna_id).order_by("nombre")
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.comuna:
            self.fields["barrio"].queryset = Barrio.objects.filter(comuna=self.instance.comuna).order_by("nombre")

        if "corregimiento" in self.data:
            try:
                corregimiento_id = int(self.data.get("corregimiento"))
                self.fields["vereda"].queryset = Vereda.objects.filter(corregimiento_id=corregimiento_id).order_by("nombre")
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.corregimiento:
            self.fields["vereda"].queryset = Vereda.objects.filter(corregimiento=self.instance.corregimiento).order_by("nombre")

    def clean(self):
        cleaned_data = super().clean()

        comuna = cleaned_data.get("comuna")
        barrio = cleaned_data.get("barrio")
        corregimiento = cleaned_data.get("corregimiento")
        vereda = cleaned_data.get("vereda")

        tiene_urbana = comuna or barrio
        tiene_rural = corregimiento or vereda

        if tiene_urbana and tiene_rural:
            raise forms.ValidationError(
                "El proyecto debe registrarse como urbano o rural, pero no ambos al mismo tiempo."
            )

        if barrio and not comuna:
            raise forms.ValidationError(
                "Si seleccionas un barrio, debes seleccionar también una comuna."
            )

        if comuna and barrio and barrio.comuna != comuna:
            raise forms.ValidationError(
                "El barrio seleccionado no pertenece a la comuna elegida."
            )

        if vereda and not corregimiento:
            raise forms.ValidationError(
                "Si seleccionas una vereda, debes seleccionar también un corregimiento."
            )

        if corregimiento and vereda and vereda.corregimiento != corregimiento:
            raise forms.ValidationError(
                "La vereda seleccionada no pertenece al corregimiento elegido."
            )

        if not tiene_urbana and not tiene_rural:
            raise forms.ValidationError(
                "Debes seleccionar una ubicación urbana o rural para el proyecto."
            )

        return cleaned_data


class ProjectAttachmentForm(forms.ModelForm):
    class Meta:
        model = ProjectAttachment
        fields = ["archivo", "descripcion"]

class ProjectReviewForm(forms.ModelForm):
    class Meta:
        model = ProjectReview
        fields = ["tipo", "observacion"]
        widgets = {
            "observacion": forms.Textarea(attrs={"rows": 3}),
        }