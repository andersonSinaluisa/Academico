from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

from mant.models import GenrGeneral
from matr.models import AnioLectivo, CabCurso, Materia, \
    DetalleMateriaCurso, Aniolectivo_curso


class AnioLectivoCrearForm(forms.ModelForm):
    class Meta:
        model = AnioLectivo
        fields = "__all__"

    def clean(self):
        anio_value = self.cleaned_data['anio']
        ciclo_value = self.cleaned_data['ciclo']
        anio_validate = AnioLectivo.objects.filter(anio=anio_value, ciclo=ciclo_value)
        if anio_validate:
            raise ValidationError(_('Ya existe un año lectivo con el año %(value)s y ciclo %(ciclo)s'),
                                  params={'value': anio_value, 'ciclo': ciclo_value})
        return super().clean()
    
    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'estado':
                if field != 'fecha_incio_ciclo' and field != 'fecha_fin_ciclo':
                    self.fields[field].widget.attrs.update({
                            'class': 'form-control'
                        })
                
        self.fields['estado'].widget.attrs.update({
            'class': 'form-check-input'
        })
        self.fields['estado'].label = _('Activo')
        self.fields['fecha_incio_ciclo'] = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
        self.fields['fecha_fin_ciclo'] = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))


class AnioLectivoEditarForm(forms.ModelForm):
    class Meta:
        model = AnioLectivo
        fields = "__all__"

    def clean(self):
        anio_value = self.cleaned_data['anio']
        ciclo_value = self.cleaned_data['ciclo']
        anio_validate = AnioLectivo.objects.filter(anio=anio_value, ciclo=ciclo_value)
        if anio_validate:
            if anio_validate.count() > 1:
                raise ValidationError(_('Ya existe un año lectivo con el año %(value)s y ciclo %(ciclo)s'),
                                    params={'value': anio_value, 'ciclo': ciclo_value})
        return super().clean()
    
    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'estado':
                if field != 'fecha_incio_ciclo' and field != 'fecha_fin_ciclo':
                    self.fields[field].widget.attrs.update({
                            'class': 'form-control'
                        })
                
        self.fields['estado'].widget.attrs.update({
            'class': 'form-check-input'
        })
        self.fields['estado'].label = _('Activo')
        self.fields['fecha_incio_ciclo'] = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
        self.fields['fecha_fin_ciclo'] = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))


class CabCursoCrearForm(forms.ModelForm):
    
    class Meta:
        model = CabCurso
        fields = "__all__"

    def clean(self):
        paralelo = self.data['paralelos']
        if len(paralelo) > 1:
            if paralelo.find(",") == -1:
                raise ValidationError(
                    _('Los paralelos deben ser separados por comas')
                )
        return super().clean()

    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        materias = Materia.objects.filter(estado=True)
        self.fields['paralelos'] = forms.CharField(max_length=255, min_length=1)
        self.fields['anio_lectivo'] = forms.ChoiceField(label=_("Año lectivo"), choices=[(i.id_anio_lectivo, str(i.anio)+"-"+str(i.ciclo))for i in AnioLectivo.objects.filter(estado=True)])
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                    'class': 'form-control'
            })
        
        self.fields['id_cfg_jornada'].queryset = GenrGeneral.objects.filter(tipo="JOR")
        self.fields['id_cfg_regimen'].queryset = GenrGeneral.objects.filter(tipo="TRE")
        self.fields['id_cfg_modalidad'].queryset = GenrGeneral.objects.filter(tipo="MOD")
        self.fields['id_cfg_tipo_edu'].queryset = GenrGeneral.objects.filter(tipo="TED")
        self.fields['id_cfg_formacion'].queryset = GenrGeneral.objects.filter(tipo="NFO")
        self.fields['paralelos'].widget.attrs.update({
                    'placeholder': 'Ejemplo: A,B,C,D,...'
            })
        self.fields['materia'] = forms.MultipleChoiceField(
            choices=[(i.id_materia, i.nombre) for i in materias],
            widget=forms.SelectMultiple(attrs={
                'class': 'choices form-select multiple-remove',
                'multiple': 'multiple'}))


class CabCursoEditarForm(forms.ModelForm):
    
    class Meta:
        model = CabCurso
        fields = "__all__"

    def clean(self):
        paralelo = self.data['paralelos']
        if paralelo:
            if len(paralelo) > 1:
                if paralelo.find(",") == -1:
                    raise ValidationError(
                        _('Los paralelos deben ser separados por comas')
                    )
        return super().clean()

    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['anio_lectivo'] = forms.ChoiceField(label=_("Año lectivo"), choices=[(i.id_anio_lectivo, str(i.anio)+"-"+str(i.ciclo))for i in AnioLectivo.objects.filter(estado=True)])
        self.fields['paralelos'] = forms.CharField(max_length=255, min_length=1)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                    'class': 'form-control'
            })
        materias = Materia.objects.filter(estado=True)
        
        self.fields['id_cfg_jornada'].queryset = GenrGeneral.objects.filter(tipo="JOR")
        self.fields['id_cfg_regimen'].queryset = GenrGeneral.objects.filter(tipo="TRE")
        self.fields['id_cfg_modalidad'].queryset = GenrGeneral.objects.filter(tipo="MOD")
        self.fields['id_cfg_tipo_edu'].queryset = GenrGeneral.objects.filter(tipo="TED")
        self.fields['id_cfg_formacion'].queryset = GenrGeneral.objects.filter(tipo="NFO")
        self.fields['paralelos'].widget.attrs.update({
                    'placeholder': 'Ejemplo: A,B,C,D,...'
            })
        self.fields['materia'] = forms.MultipleChoiceField(
            choices=[(i.id_materia, i.nombre) for i in materias],
            widget=forms.SelectMultiple(attrs={
                'class': 'choices form-select multiple-remove',
                'multiple': 'multiple'}))


class MateriaCrearForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = "__all__" 

    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'estado':
                self.fields[field].widget.attrs.update({
                        'class': 'form-control'
                })
            else:
                self.fields[field].widget.attrs.update({
                        'class': 'form-check-input'
                })
        self.fields['estado'].label = _("Activo")


class MateriaProfesorForm(forms.Form):

    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['cursos'] = forms.ChoiceField(
            choices=[(i.id_curso, i.nombre)for i in CabCurso.objects.all()],
            widget=forms.Select())
        self.fields['paralelos'] = forms.ChoiceField(
            choices=[
                (i.id_matr_anioelectivo_curso, i.paralelo)
                for i in Aniolectivo_curso.objects.filter(
            estado=True, id_anio_electivo__estado=True
            )], widget=forms.Select())
        
        self.fields['materias'] = forms.MultipleChoiceField(
            choices=[(i.id_detalle_materia_curso, i.id_materia.nombre)
            for i in DetalleMateriaCurso.objects.filter(
            estado=True,
            id_matr_anio_lectivo_curso__estado=True)])
        
        for field in iter(self.fields):
            if field != 'materias':
                self.fields[field].widget.attrs.update({
                        'class': 'form-control'
                })
            else:
                self.fields[field].widget.attrs.update({
                        
                })
