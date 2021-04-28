from django.shortcuts import render, redirect, render_to_response
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
from django.contrib.auth.models import Permission, Group
from django.views.defaults import page_not_found
 
def pag_404_not_found(request, exception, template_name="error/404.html"):
    response = render_to_response("../templates/page_404.html")
    response.status_code=404
    return response


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

    def get_context_data(self, **kwargs):
        context = {}
        context = super(ModuloCrear, self).get_context_data(**kwargs)
        context['url'] = self.success_url
        context['accion'] = 'Crear'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modulo guardado correctamente')
            return render(request,self.template_name,self.get_context_data(form=form))
        else:
            return render(request,self.template_name,self.get_context_data(form=form))

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
    def get_context_data(self, **kwargs):
        context = {}
        context = super(ModuloEditar, self).get_context_data(**kwargs)
        context['url'] = self.success_url
        context['accion'] = 'Editar'
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        obj = self.model.objects.get(id_modulo=kwargs['pk'])
        print(obj)
        form = self.form_class(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modulo guardado correctamente')
            return render(request,self.template_name,self.get_context_data(form=form))
        else:
            return render(request,self.template_name,self.get_context_data(form=form))

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
        context['accion'] = 'Crear'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menú creado correctamente')
            return render(request,self.template_name,self.get_context_data(form=form))
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
        context['accion'] = 'Editar'
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
            return render(request,self.template_name,self.get_context_data(form=form))

class PermisosListar(ListView):
    model = Group
    template_name ="roles/listar_rol.html"
    permission_required = "auth.view_group"
    context_object_name = 'obj'
    login_url = "/"

class PermisosCrear(CreateView):
    model = Group
    template_name = "roles/crear_rol.html"
    form_class = RolesPermisosForm
    success_url = reverse_lazy('cfg:roles')
    permission_required = "auth.add_group"

    def get_context_data(self, **kwargs):
        context = {}
        context = super(PermisosCrear, self).get_context_data(**kwargs)
        context['url'] = self.success_url
        context['accion'] = 'Crear'
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            c = form.save()
            for i in form.cleaned_data:
                valor = form.cleaned_data[i]
                permiso = Permission.objects.filter(codename=i).first()
                if permiso and valor:
                    c.permissions.add(permiso.id)
            messages.success(request,_('Nuevo Rol creado correctamente'))
            return render(request, self.template_name, self.get_context_data(form=form))
        else:
            return render(request, self.template_name, self.get_context_data(form=form))



class PermisosEditar(UpdateView):
    model = Group
    template_name = "roles/crear_rol.html"
    form_class = GrupoPermisoEditForm
    success_url = reverse_lazy('cfg:roles')
    permission_required = "auth.change_group"

    def get_context_data(self, **kwargs):
        context = {}
        context = super(PermisosEditar, self).get_context_data(**kwargs)
        context['url'] = self.success_url
        context['accion'] = 'Editar'
        return context
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.object = self.get_object
        obj = self.model.objects.get(pk=pk)
        form = self.form_class(instance=obj)
        permisos = obj.permissions.all()
        context = {}
        for i in form:
            if i.name != 'name':
                a = permisos.filter(codename=i.name) 
                if a:
                    valor = i.field.widget.check_test(i.value())
                    if not valor:
                        context[i.name] = True
            else:
                context[i.name] = i.value()
        form = self.form_class(data=context,instance=obj)
        return render(request, self.template_name, self.get_context_data(form=form))
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        obj = self.model.objects.get(pk=kwargs['pk'])
        form = self.form_class(request.POST,instance=obj)
        if form.is_valid():
            c = form.save()
            for i in form.cleaned_data:
                valor = form.cleaned_data[i]
                permiso = Permission.objects.filter(codename=i).first()
                if permiso and valor:
                    c.permissions.add(permiso.id)
            messages.success(request,_('Rol guardado correctamente'))
            return render(request, self.template_name, self.get_context_data(form=form))
        else:
            return render(request, self.template_name, self.get_context_data(form=form))


            return render(request, self.template_name, self.get_context_data(form=form))


class GeneralCrear(PermissionRequiredMixin, CreateView):
    """Clase para crear un atributo en gen_general donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """

    model = GenrGeneral
    template_name = 'general/crear_general.html'
    permission_required = "cfg.add_genrgeneral"
    form_class = GeneralForm
    success_url = reverse_lazy('cfg:general')
    login_url = "/"


class GeneralListar(PermissionRequiredMixin, ListView):
    """Clase para listar la tabla gen_general donde permission_required
    Especifica que permiso debe tener el usuario para acceder
    a la pantalla """

    model = GenrGeneral
    template_name = 'general/listar_general.html'
    permission_required = "cfg.view_genrgeneral"
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
