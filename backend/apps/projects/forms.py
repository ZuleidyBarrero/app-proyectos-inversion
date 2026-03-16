from django import forms
from .models import Project, ProjectAttachment


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

        if comuna and barrio:
            if barrio.comuna != comuna:
                raise forms.ValidationError(
                    "El barrio seleccionado no pertenece a la comuna elegida."
                )

        if vereda and not corregimiento:
            raise forms.ValidationError(
                "Si seleccionas una vereda, debes seleccionar también un corregimiento."
            )

        if corregimiento and vereda:
            if vereda.corregimiento != corregimiento:
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