from django import forms
from mant.models import *


class PersonaForm(forms.ModelForm):
    """Formulario para crear persona"""
    class Meta:
        model = Persona
        fields = [
            "nombres",
            "apellidos",
        ]


class PersonaEditForm(forms.ModelForm):
    """Formulario para editar persona"""
    class Meta:
        model = Persona
        fields = [
            "nombres",
            "apellidos",
        ]