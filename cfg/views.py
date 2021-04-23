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
from cfg.models import Modulo, Menu
from cfg.forms import ModuloForm, MenuForm, ModuloEditForm, MenuEditForm
# Create your views here.

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
    return render(request,'login.html',context)

@login_required(login_url='/')
def inicio(request):
    return render(request,'inicio.html')


class ModuloCrear(PermissionRequiredMixin, CreateView):
    """Clase para crear un modulo donde permission_required"""
    """Especifica que permiso debe tener el usuario para acceder"""
    """a la pantalla """

    model = Modulo
    template_name = 'modulos/crear_modulo.html'
    permission_required = "cfg.add_modulo"
    form_class = ModuloForm
    success_url = reverse_lazy('cfg:modulos')


class ModuloListar(PermissionRequiredMixin,ListView):
    """Clase para listar los modulos donde permission_required"""
    """Especifica que permiso debe tener el usuario para acceder"""
    """a la pantalla """
    
    model = Modulo
    template_name = 'modulos/lista_modulo.html'
    permission_required = "cfg.view_modulo"
    context_object_name = 'obj'

class ModuloEditar(PermissionRequiredMixin,UpdateView):
    """Clase para editar un modulo donde permission_required"""
    """Especifica que permiso debe tener el usuario para acceder"""
    """a la pantalla """

    model = Modulo
    template_name = 'modulos/crear_modulo.html'
    permission_required = "cfg.change_modulo"
    form_class = ModuloEditForm
    success_url = reverse_lazy('cfg:modulos') 


class MenuListar(PermissionRequiredMixin, ListView):
    model = Menu
    template_name = 'menus/listar_menu.html'
    permission_required = "cfg.view_menu"
    context_object_name = 'obj'

class MenuCrear(PermissionRequiredMixin,CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menus/crear_menu.html'
    permission_required="cfg.add_menu"
    success_url = reverse_lazy("cfg:menus")

class MenuEditar(PermissionRequiredMixin, UpdateView):
    """Clase para editar un menu donde permission_required"""
    """Especifica que permiso debe tener el usuario para acceder"""
    """a la pantalla """

    model = Modulo
    template_name = 'menus/crear_menu.html'
    permission_required = "cfg.change_menu"
    form_class = MenuEditForm
    success_url = reverse_lazy('cfg:menus') 