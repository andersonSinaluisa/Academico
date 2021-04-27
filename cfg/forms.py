from django import forms
from cfg.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.contrib.auth.models import Group, Permission
from django.db.models import Q


class ModuloForm(forms.ModelForm):
    """formulario para crear modulo"""

    class Meta:
        model = Modulo
        fields = '__all__'

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
            if field != 'estado':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class ModuloEditForm(forms.ModelForm):
    """formulario para crear modulo"""

    class Meta:
        model = Modulo
        fields = '__all__'

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
        # añade atributos html al formulario
        self.fields['estado'].widget.attrs.update({
            'class': 'form-check-input'
        })
        self.fields['url_menu'].widget.attrs.update({
            'placeholder': 'Ejemplo: /roles/'
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



class GrupoPermisoEditForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        permisos = Permission.objects.filter(~Q(content_type__model='logentry')| ~Q(content_type__model='contenttype') | ~Q(content_type__model='session'))
        for permiso in permisos:
            val1 = permiso.name.find('Can change')
            val2 = permiso.name.find('Can view')
            val3 = permiso.name.find('Can add')
            val4 = permiso.name.find('Can delete')
            if val1 !=-1:
                name_permiso = permiso.name.replace('Can change','Editar')
            elif val2 !=-1:
                name_permiso = permiso.name.replace('Can view','Ver')
            elif val3 !=-1:
                name_permiso = permiso.name.replace('Can add','Agregar')
            elif val4 !=-1:
                name_permiso = permiso.name.replace('Can delete','Eliminar')
            self.fields[permiso.codename] = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),label=name_permiso,required=False)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        
class RolesPermisosForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

    def clean(self):
        name = self.data['name']
        grupo = Group.objects.filter(name=name)
        if grupo:
            raise ValidationError(
                                    _('Ya existe un rol con la descripción %(value)s.'),
                                    params={'value': name},
                                )
        return super().clean()
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        permisos = Permission.objects.filter(~Q(content_type__model='logentry')| ~Q(content_type__model='contenttype') | ~Q(content_type__model='session'))
        for permiso in permisos:
            val1 = permiso.name.find('Can change')
            val2 = permiso.name.find('Can view')
            val3 = permiso.name.find('Can add')
            val4 = permiso.name.find('Can delete')
            if val1 !=-1:
                name_permiso = permiso.name.replace('Can change','Editar')
            elif val2 !=-1:
                name_permiso = permiso.name.replace('Can view','Ver')
            elif val3 !=-1:
                name_permiso = permiso.name.replace('Can add','Agregar')
            elif val4 !=-1:
                name_permiso = permiso.name.replace('Can delete','Eliminar')
            self.fields[permiso.codename] = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),label=name_permiso,required=False)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})



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
