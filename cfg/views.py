from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.models import User
from cfg.backend import EmailBackend
from django.contrib.auth import login as do_login
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView
from cfg.models import *
from cfg.forms import *
from django.contrib import messages


def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = EmailBackend.authenticate(
            EmailBackend,
            request,
            username,
            password
        )
        if user is not None:
            do_login(request, user)
            return redirect(reverse_lazy('cfg:inicio'))
        else:
            context['msj'] = _('Usuario y/o contraseña incorrecta')
    return render(request, 'login.html', context)


@login_required(login_url='/')
def inicio(request):
    return render(request, 'inicio.html')


class ModuloCrear(PermissionRequiredMixin, CreateView):
    """Clase para crear un modulo donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """

    model = Modulo
    template_name = 'modulos/crear_modulo.html'
    permission_required = "cfg.add_modulo"
    form_class = ModuloForm
    success_url = reverse_lazy('cfg:modulos')
    login_url = "/"


class ModuloListar(PermissionRequiredMixin, ListView):
    """Clase para listar los modulos donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """

    model = Modulo
    template_name = 'modulos/lista_modulo.html'
    permission_required = "cfg.view_modulo"
    context_object_name = 'obj'
    login_url = "/"


class ModuloEditar(PermissionRequiredMixin, UpdateView):
    """Clase para editar un modulo donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """

    model = Modulo
    template_name = 'modulos/crear_modulo.html'
    permission_required = "cfg.change_modulo"
    form_class = ModuloEditForm
    login_url = "/"
    success_url = reverse_lazy('cfg:modulos')


class MenuListar(PermissionRequiredMixin, ListView):
    model = Menu
    template_name = 'menus/listar_menu.html'
    permission_required = "cfg.view_menu"
    context_object_name = 'obj'
    login_url = "/"


class MenuCrear(PermissionRequiredMixin, CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menus/crear_menu.html'
    permission_required = "cfg.add_menu"
    success_url = reverse_lazy("cfg:menus")
    login_url = "/"

    def get_context_data(self, **kwargs):
        context = super(MenuCrear, self).get_context_data(**kwargs)
        context['url'] = self.success_url
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menú creador correctamente')
            return render(request, self.template_name, self.get_context_data(form=form))
        else:
            return render(request, self.template_name, self.get_context_data(form=form))


class MenuEditar(PermissionRequiredMixin, UpdateView):
    """Clase para editar un menu donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """

    model = Menu
    template_name = 'menus/crear_menu.html'
    permission_required = "cfg.change_menu"
    form_class = MenuEditForm
    success_url = reverse_lazy('cfg:menus')
    login_url = "/"

    def get_context_data(self, **kwargs):
        context = super(MenuEditar, self).get_context_data(**kwargs)
        context['url'] = self.success_url
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        obj = self.model.objects.get(id_menu=kwargs['pk'])
        print(obj)
        form = self.form_class(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menú guardado correctamente')
            return render(request, self.template_name, self.get_context_data(form=form))
        else:
            return render(request, self.template_name, self.get_context_data(form=form))


class GeneralCrear(PermissionRequiredMixin, CreateView):
    """Clase para crear un atributo en gen_general donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """

    model = GenrGeneral
    template_name = 'general/crear_general.html'
    permission_required = "cfg.add_general"
    form_class = GeneralForm
    success_url = reverse_lazy('cfg:general')
    login_url = "/"


class GeneralListar(PermissionRequiredMixin, ListView):
    """Clase para listar la tabla gen_general donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """

    model = GenrGeneral
    template_name = 'general/listar_general.html'
    permission_required = "cfg.view_general"
    context_object_name = 'obj'
    login_url = "/"


class GeneralEditar(PermissionRequiredMixin, UpdateView):
    """Clase para editar un atributo en gen_general donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """

    model = GenrGeneral
    template_name = 'general/crear_general.html'
    permission_required = "cfg.change_general"
    form_class = GeneralEditForm
    login_url = "/"
    success_url = reverse_lazy('cfg:general')
