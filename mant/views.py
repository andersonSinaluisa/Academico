from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from mant.forms import PersonaForm, PersonaEditForm
from mant.models import Persona
from django.contrib.auth.models import Group, User
from django.contrib.auth.hashers import make_password
from random import choice
from django.shortcuts import render, reverse, redirect


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

    def generate_password(self, request):
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
            tmp_pass, password = self.generate_password(request)
            user = User(username=c.identificacion,password=password,first_name=c.nombres,last_name=c.apellidos)
            user.save()
            grupo = Group.objects.filter(pk = form.cleaned_data['rol']).first()
            grupo.user_set.add(user)
            
        return render(request, self.template_name, self.get_context_data(form=form))

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