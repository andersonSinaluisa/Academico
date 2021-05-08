from django.shortcuts import render
from matr.models import AnioLectivo, CabCurso, Aniolectivo_curso, Materia,\
    DetalleMateriaCurso
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from matr.forms import AnioLectivoCrearForm, AnioLectivoEditarForm, CabCursoCrearForm,\
    MateriaCrearForm, CabCursoEditarForm
from django.urls import reverse_lazy
from django.contrib import messages
from mant.models import GenrGeneral
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


# Create your views here.
class AnioLectivoCrear(PermissionRequiredMixin,CreateView):
    model = AnioLectivo
    form_class = AnioLectivoCrearForm
    permission_required = "matr.add_aniolectivo"
    template_name = "anio_lectivo/crear_anio_lectivo.html"
    login_url = "/"
    success_url = reverse_lazy('matr:anios_lectivo')

    def get_context_data(self, **kwargs):
        context = super(AnioLectivoCrear,self).get_context_data(**kwargs)
        context['url'] = self.success_url
        context['accion'] = 'Crear'
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Año lectivo creado correctamente')
            return render(request, self.template_name, self.get_context_data(form=form))
        else:
            return render(request, self.template_name, self.get_context_data(form=form))

class AnioLectivoListar(PermissionRequiredMixin,ListView):
    model = AnioLectivo
    template_name = "anio_lectivo/listar_anio_lectivo.html"
    context_object_name = 'obj'
    permission_required = "matr.view_aniolectivo"
    login_url = "/"


class AnioLectivoEditar(PermissionRequiredMixin,UpdateView):
    model = AnioLectivo
    form_class = AnioLectivoEditarForm
    permission_required = "matr.change_aniolectivo"
    template_name = "anio_lectivo/crear_anio_lectivo.html"
    login_url = "/"
    success_url = reverse_lazy('matr:anios_lectivo')

    def get_context_data(self, **kwargs):
        context = super(AnioLectivoEditar,self).get_context_data(**kwargs)
        context['url'] = self.success_url
        context['accion'] = 'Editar'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            c = form.save()
            messages.success(request, 'Año lectivo creado correctamente')
            return render(request, self.template_name, self.get_context_data(form=form))
        else:
            return render(request, self.template_name, self.get_context_data(form=form))


class CabCursoCrear(PermissionRequiredMixin,CreateView):
    model = CabCurso
    form_class = CabCursoCrearForm
    permission_required = "matr.add_cabcurso"
    template_name = "curso/crear_curso.html"
    login_url = "/"
    success_url = reverse_lazy('matr:cursos')

    def get_context_data(self, **kwargs):
        context = super(CabCursoCrear,self).get_context_data(**kwargs)
        materia = Materia.objects.filter(estado=True)
        if not materia:
            context['alert'] = _("Se deben crear las materias")
        context['url'] = self.success_url
        context['accion'] = 'Crear'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            dict_data = dict(form.data)
            c = form.save()
            if form.cleaned_data['paralelos']:
                paralelos = form.cleaned_data['paralelos']
                curso_detalle = None
                for i in paralelos.split(','):
                    curso_detalle = Aniolectivo_curso.objects.create(
                        id_anio_electivo_id=form.cleaned_data['anio_lectivo'],
                        id_curso=c,
                        paralelo=i,
                        estado=True,
                        cupos=form.cleaned_data['cupo']
                        )
                if curso_detalle:
                    for valor in form.cleaned_data['materia']:
                        hora = int(dict_data[valor][0])
                        DetalleMateriaCurso.objects.create(
                            id_matr_anio_lectivo_curso=curso_detalle,
                            total_horas=hora,
                            id_materia_id=valor,
                            estado=True
                        )
                    

            messages.success(request, 'Curso creado correctamente')
            return render(request, self.template_name, self.get_context_data(form=form))
        else:
            return render(request, self.template_name, self.get_context_data(form=form))

class CabCursoLista(PermissionRequiredMixin,ListView):
    model = CabCurso
    template_name = "curso/listar_curso.html"
    context_object_name = 'obj'
    permission_required = "matr.view_cabcurso"
    login_url = "/"


class CabCursoEditar(PermissionRequiredMixin,UpdateView):
    model = CabCurso
    form_class = CabCursoEditarForm
    permission_required = "matr.add_cabcurso"
    template_name = "curso/crear_curso.html"
    login_url = "/"
    success_url = reverse_lazy('matr:cursos')

    def get_context_data(self, **kwargs):
        context = super(CabCursoEditar,self).get_context_data(**kwargs)
        materia = Materia.objects.filter(estado=True)
        if not materia:
            context['alert'] = _("Se deben crear las materias")
        context['url'] = self.success_url
        context['accion'] = 'Editar'
        return context
    
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.object = self.get_object
        obj = self.model.objects.get(pk=pk)
        form = self.form_class(instance=obj)
        context = {}
        if obj:
            detalle = DetalleMateriaCurso.objects.filter(
                id_matr_anio_lectivo_curso__id_curso=obj
                )
            if detalle:
                array_materias = [materia.id_materia.id_materia for materia in detalle]
                for i in form:
                    if i.name != 'materia':
                        context[i.name] = i.value()
                    else:
                        print(i.name,i.value())
        return super().get(request, *args, **kwargs)
    
class MateriasLista(PermissionRequiredMixin,ListView):
    model = Materia
    template_name = "materia/listar_materias.html"
    context_object_name = 'obj'
    permission_required = "matr.view_materia"
    login_url = "/"


class MateriasCrear(PermissionRequiredMixin,CreateView):
    model = Materia
    form_class = MateriaCrearForm
    template_name = "materia/crear_materia.html"
    login_url = "/"
    success_url = reverse_lazy('matr:materias')
    permission_required = "matr.add_materia"

    def get_context_data(self, **kwargs):
        context = super(MateriasCrear,self).get_context_data(**kwargs)
        context['url'] = self.success_url
        context['accion'] = 'Crear'
        return context

class MateriasEditar(PermissionRequiredMixin,UpdateView):
    model = Materia
    form_class = MateriaCrearForm
    template_name = "materia/crear_materia.html"
    login_url = "/"
    success_url = reverse_lazy('matr:materias')
    permission_required = "matr.add_materia"

    def get_context_data(self, **kwargs):
        context = super(MateriasEditar,self).get_context_data(**kwargs)
        context['url'] = self.success_url
        context['accion'] = 'Editar'
        return context

