from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
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
        context = {}
        context = super(PersonaCrear, self).get_context_data(**kwargs)
        context['url'] = self.success_url
        context['accion'] = 'Editar'
        return context

class PersonaEditar(PermissionRequiredMixin, UpdateView):
    """Clase para editar a una persona donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """

    model = Persona
    template_name = 'persona/editar_persona.html'
    permission_required = "mant.change_persona"
    form_class = PersonaEditForm
    success_url = reverse_lazy('mant:personas')
    def get_context_data(self, **kwargs):
        context = {}
        context = super(PersonaEditar, self).get_context_data(**kwargs)
        context['url'] = self.success_url
        context['accion'] = 'Editar'
        return context