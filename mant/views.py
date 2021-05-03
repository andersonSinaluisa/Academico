from random import choice

from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group, User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from mant.forms import PersonaForm, PersonaEditForm
from mant.models import Persona


class PersonaListar(PermissionRequiredMixin, ListView):
    """Clase para crear a una persona donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """
    model = Persona
    template_name = "persona/listar_persona.html"
    permission_required = "mant.view_persona"
    context_object_name = "obj"


class PersonaCrear(PermissionRequiredMixin, CreateView):
    """Clase para editar a una persona donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """
    model = Persona
    form_class = PersonaForm
    template_name = 'persona/crear_persona.html'
    permission_required = "mant.add_persona"
    success_url = reverse_lazy("mant:personas")

    def get_context_data(self, **kwargs):
        context = super(PersonaCrear, self).get_context_data(**kwargs)
        context['url'] = self.success_url
        context['accion'] = 'Editar'
        return context

    @staticmethod
    def generate_password(request):
        longitud = 6
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        tmp_pass = ""
        tmp_pass = tmp_pass.join([choice(valores) for i in range(longitud)])
        tmp_pass.replace(" ", "")
        password = make_password(tmp_pass, salt=None, hasher='default')
        return tmp_pass, password

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            c = form.save()
            is_empleado = form.cleaned_data['is_empleado']
            if is_empleado:
                c.pnombres = None
                c.papellidos = None
                c.pidentificacion = None
                c.pdireccion = None
                c.ptelefono = None
                c.pvive_con_usted = None
                c.id_cfg_estado_laboralp = None
                c.mnombres = None
                c.mapellidos = None
                c.midentificacion = None
                c.mdireccion = None
                c.mtelefono = None
                c.mvive_con_usted = None
                c.id_cfg_estado_laboralm = None
                c.bono_solidario = None
                c.rnombres = None
                c.rapellidos = None
                c.rtelefono = None
                c.id_cfg_tipo_identificacion = None
                c.ridentificacion = None
                c.tipo_parentesco = None
                c.rvive_con_usted = None
                c.rdireccion_trabajo = None
                c.rtelefono_trabajo = None
                c.rcorreo = None
                c.rhorario_laboral = None
                c.miembros_hogar = None
                c.save()
            tmp_pass, password = self.generate_password(request)
            user = User(username=c.identificacion, password=password, first_name=c.nombres, last_name=c.apellidos)
            user.save()
            grupo = Group.objects.filter(pk=form.cleaned_data['rol']).first()
            grupo.user_set.add(user)

        return render(request, self.template_name, self.get_context_data(form=form))


class PersonaEditar(PermissionRequiredMixin, UpdateView):
    """Clase para editar a una persona donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """

    model = Persona
    template_name = 'persona/crear_persona.html'
    permission_required = "mant.change_persona"
    form_class = PersonaEditForm
    success_url = reverse_lazy('mant:personas')

    def get_context_data(self, **kwargs):
        context = super(PersonaEditar, self).get_context_data(**kwargs)
        context['url'] = self.success_url
        context['accion'] = 'Editar'
        return context


class PersonaEliminar(PermissionRequiredMixin, DeleteView):
    """Clase para eliminar a una persona donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """
    model = Persona
    template_name = 'persona/eliminar_persona.html'
    success_url = reverse_lazy('mant:personas')
    permission_required = "mant.delete_persona"
    login_url = "/"
