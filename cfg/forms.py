from django import forms
from cfg.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class ModuloForm(forms.ModelForm):
    """formulario para crear modulo"""

    class Meta:
        model = Modulo
        fields = [
            'codigo',
            'nombre',
            'icono',
            'orden'
        ]

    def clean(self):
        """metodo donde se realizan las validaciones"""
        orden = self.cleaned_data['orden']
        nombre = self.cleaned_data['nombre']
        modulo = Modulo.objects.filter(orden=orden, estado=True)
        nombre_modulo = Modulo.objects.filter(nombre=nombre)
        if modulo:
            raise ValidationError(
                _('Ya existe un modulo en la posición %(value)s '),
                params={'value': orden},
            )
        if nombre_modulo:
            raise ValidationError(
                _('Ya existe un modulo con el nombre %(value)s '),
                params={'value': nombre},
            )
        return super().clean()

    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ModuloEditForm(forms.ModelForm):
    """formulario para crear modulo"""

    class Meta:
        model = Modulo
        fields = [
            'codigo',
            'nombre',
            'icono',
            'orden'
        ]

    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"

    def clean(self):
        nombre = self.cleaned_data['nombre']
        menu = Menu.objects.filter(nombre=nombre)
        if menu:
            raise ValidationError(_('Ya existe un menú con el nombre %(value)s '),
                                  params={'value': nombre})
        return super().clean()

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
        self.fields['estado'].widget.attrs.update({
            'class': 'form-check-input'
        })


class MenuEditForm(forms.ModelForm):
    class Meta:
        model = Menu
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
        self.fields['estado'].widget.attrs.update({
            'class': 'form-check-input'
        })


class GeneralForm(forms.ModelForm):
    """formulario para crear un campo en la tabla general"""

    class Meta:
        model = GenrGeneral
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class GeneralEditForm(forms.ModelForm):
    """formulario para editar un campo en la tabla general"""

    class Meta:
        model = GenrGeneral
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """inicializa los widgets para poner class form-control
        en los input"""

        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })