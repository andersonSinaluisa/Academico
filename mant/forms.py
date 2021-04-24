from django import forms
from mant.models import Persona


class PersonaForm(forms.ModelForm):
    """Formulario para crear persona"""

    class Meta:
        model = Persona
        fields = "__all__"
        exclude = {
            "id_persona",
            "estado",
            "fecha_ingreso",
            "usuario_ing",
            "terminal_ing",
            "is_estudiante",
            "is_empleado",
            "is_representante"
        }

    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class PersonaEditForm(forms.ModelForm):
    """Formulario para editar persona"""

    class Meta:
        model = Persona
        fields = "__all__"
        exclude = {
            "id_persona",
            "estado",
            "fecha_ingreso",
            "usuario_ing",
            "terminal_ing",
            "is_estudiante",
            "is_empleado",
            "is_representante"
        }

    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
