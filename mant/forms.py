from django import forms
from mant.models import Persona, GenrGeneral
from django.contrib.auth.models import Group
from django.db.models import Q


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
            "id_usuario"
        }

    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['rol'] = forms.ChoiceField(choices=[(i.pk,i.name)for i in Group.objects.all()])
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['is_estudiante'] = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),label='Es Estudiantes')
        self.fields['is_empleado'] = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),label='Es Empleado')
        self.fields['is_representante'] = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),label='Es Representante')
        self.fields['id_cfg_tipo_identificacion'].queryset = GenrGeneral.objects.filter(tipo='TID')

        self.fields['id_cfg_genero'].queryset = GenrGeneral.objects.filter(tipo='GEN')
        self.fields['id_cfg_pais'].queryset = GenrGeneral.objects.filter(tipo='TPA')
        self.fields['id_cfg_estado_civil'].queryset = GenrGeneral.objects.filter(tipo='EST')
        self.fields['id_cfg_tipo_sangre'].queryset = GenrGeneral.objects.filter(tipo='TSA')
        self.fields['id_cfg_etnia'].queryset = GenrGeneral.objects.filter(tipo='ETN')
        self.fields['id_cfg_jornada'].queryset = GenrGeneral.objects.filter(tipo='JOR')
        self.fields['id_cfg_indigena'].queryset = GenrGeneral.objects.filter(tipo='IDA')
        self.fields['id_cfg_idioma_ancestral'].queryset = GenrGeneral.objects.filter(tipo='IDA')
        self.fields['id_cfg_provincia'].queryset = GenrGeneral.objects.filter(tipo='593')
        self.fields['id_cfg_ciudad'].queryset = GenrGeneral.objects.filter(tipo__lt=24)
        self.fields['id_cfg_categoria_migratoria'].queryset = GenrGeneral.objects.filter(tipo='CMI')
        self.fields['id_cfg_estado_civil'].queryset = GenrGeneral.objects.filter(tipo='EST')
        self.fields['id_cfg_estado_laboralp'].queryset = GenrGeneral.objects.filter(tipo='ESTL')

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
            "id_usuario"
        }

    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['rol'] = forms.ChoiceField(choices=[(i.pk,i.name)for i in Group.objects.all()])
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        
        self.fields['is_estudiante'] = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),label='Es Estudiantes')
        self.fields['is_empleado'] = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),label='Es Empleado')
        self.fields['is_representante'] = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),label='Es Representante')
        self.fields['id_cfg_tipo_identificacion'].queryset = GenrGeneral.objects.filter(tipo='TID')

        self.fields['id_cfg_genero'].queryset = GenrGeneral.objects.filter(tipo='GEN')
        self.fields['id_cfg_pais'].queryset = GenrGeneral.objects.filter(tipo='TPA')
        self.fields['id_cfg_estado_civil'].queryset = GenrGeneral.objects.filter(tipo='EST')
        self.fields['id_cfg_tipo_sangre'].queryset = GenrGeneral.objects.filter(tipo='TSA')
        self.fields['id_cfg_etnia'].queryset = GenrGeneral.objects.filter(tipo='ETN')
        self.fields['id_cfg_jornada'].queryset = GenrGeneral.objects.filter(tipo='JOR')
        self.fields['id_cfg_indigena'].queryset = GenrGeneral.objects.filter(tipo='IDA')
        self.fields['id_cfg_idioma_ancestral'].queryset = GenrGeneral.objects.filter(tipo='IDA')
        self.fields['id_cfg_provincia'].queryset = GenrGeneral.objects.filter(tipo='593')
        self.fields['id_cfg_ciudad'].queryset = GenrGeneral.objects.filter(tipo__lt=24)
        self.fields['id_cfg_categoria_migratoria'].queryset = GenrGeneral.objects.filter(tipo='CMI')
        self.fields['id_cfg_estado_civil'].queryset = GenrGeneral.objects.filter(tipo='EST')
        self.fields['id_cfg_estado_laboralp'].queryset = GenrGeneral.objects.filter(tipo='ESTL')