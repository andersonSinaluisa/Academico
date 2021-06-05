from typing import ClassVar
from django.http.response import JsonResponse
from django.shortcuts import render
from matr.models import AnioLectivo, CabCurso, Aniolectivo_curso, Materia,\
    DetalleMateriaCurso, Materia_profesor
from mant.models import Persona
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from matr.forms import AnioLectivoCrearForm, AnioLectivoEditarForm, CabCursoCrearForm,\
    MateriaCrearForm, CabCursoEditarForm, MateriaProfesorForm, MateriaProfesorForm
from django.urls import reverse_lazy
from django.contrib import messages
from mant.models import GenrGeneral
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import json

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
            print(dict_data)
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
        obj = self.model.objects.filter(id_curso=pk).first()
        form = self.form_class(instance=obj)
        context = {}
        if obj:
            detalle = DetalleMateriaCurso.objects.filter(
                id_matr_anio_lectivo_curso__id_curso=obj
                )
            detalle_curso = Aniolectivo_curso.objects.filter(id_curso=obj).order_by('-paralelo')
            if detalle and detalle_curso:
                paralelos = ""
                for x in detalle_curso:
                    paralelos = x.paralelo+","+paralelos
                paralelos = paralelos[:-1]
                
                array_materias = [str(materia.id_materia.id_materia) for materia in detalle]
                for i in form:
                    if i.name == 'materia':
                        context[i.name] = array_materias if array_materias else None

                    elif i.name=='paralelos':
                        context[i.name] = paralelos
                    
                    elif i.name =='anio_lectivo':
                        context[i.name] = detalle_curso.first().id_anio_electivo_id
                    else:
                        context[i.name] = i.value()
                
                for materia_detalle in detalle:
                    context[str(materia_detalle.id_materia.id_materia)] = [str(materia_detalle.total_horas)]
        form = self.form_class(data=context, instance=obj)
        return render(request, self.template_name, self.get_context_data(form=form))
    
class CursoDetalle(TemplateView):
    model = CabCurso
    template_name = "curso/curso_detalle.html"
    
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        curso = CabCurso.objects.filter(id_curso=pk).first()
        paralelos = Aniolectivo_curso.objects.filter(id_curso=curso)
        lista_final = []
        for i in paralelos:
            materias = DetalleMateriaCurso.objects.filter(id_matr_anio_lectivo_curso=i)
            lista_materias = []
            for m in materias:
                lista_materias.append({
                    "materia":m.id_materia.nombre,
                    "horas":m.total_horas
                })
            lista_final.append(
                {
                    "paralelo":i.paralelo,
                    "cupos":i.cupos,
                    "materias":lista_materias
                }
            )
        
        context = {
            "curso":curso,
            "paralelos":lista_final
        }
        return render(request,self.template_name,self.get_context_data(form=context))


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


class AsignacionMateriaProfesor(PermissionRequiredMixin,ListView):
    model = Persona
    template_name = "asignaciones/materia_profesor.html"
    success_url = reverse_lazy('matr:materias')
    permission_required = "matr.view_materia_profesor"
    context_object_name = "obj"

    def get_queryset(self):
        return self.model.objects.filter(is_empleado=True)

class AsignacionesCrear(PermissionRequiredMixin,TemplateView):
    template_name = "asignaciones/materia_asignar.html"
    permission_required = "matr.add_materia_profesor"


    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        context  = {}
        
        cursos = CabCurso.objects.all()
        if cursos:
            paralelos = Aniolectivo_curso.objects.filter(id_curso__in=cursos,estado=True,id_anio_electivo__estado=True)
            context['cursos'] = cursos
            context['paralelos'] = paralelos
        else:
            context['msj'] = _("No existen cursos")
        return render(request,self.template_name,context)



def conultar_materias_paralelo(request):
    """Consulta las meterias que pertenecen
    a un paralelo

    Args:
        request ([POST]):
        {
            'id_paralelo':int
        }

    Returns:
        [JsonResponse]: 
        [
            {
                'materia':str,
                'id':int,
                'hora':int,
                'curso':str,
                'paralelo':str,
                'id_curso':int
            }
        ]
    """
    lista = []
    if request.method=='POST':
        id_paralelo = request.POST['id_paralelo']
        print(id_paralelo)
        materias = DetalleMateriaCurso.objects.filter(
            id_matr_anio_lectivo_curso=id_paralelo,estado=True
            )
        for i in materias:
            lista.append(
                {
                    "materia":i.id_materia.nombre,
                    "id":i.id_detalle_materia_curso,
                    "hora":i.total_horas,
                    "curso":i.id_matr_anio_lectivo_curso.id_curso.nombre,
                    "paralelo":i.id_matr_anio_lectivo_curso.paralelo,
                    "id_curso":i.id_matr_anio_lectivo_curso.id_curso.id_curso
                }
            )
        if lista:
            return JsonResponse({"res":lista,"val":True})
        else:
            return JsonResponse({"res":lista,"val":False})



class AsignarHoraMateria(TemplateView):
    template_name = 'asignaciones/hora_materia.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        materia = DetalleMateriaCurso.objects.filter(id_detalle_materia_curso=pk)
        return render(request,self.template_name,self.get_context_data(materia=materia))



def guardar_horario_profesor(request):
    if request.method=='POST':
        lista = request.POST.getlist('lista[]')
        datos_list = json.loads(lista[0])
        for i in datos_list:
            print(i)
        return JsonResponse({})
        
