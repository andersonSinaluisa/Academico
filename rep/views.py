from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from matr.models import *
from openpyxl import Workbook


class ReporteCurso(PermissionRequiredMixin, TemplateView):
    # Clase para generar el reporte de un grupo de estudiantes
    template_name = "rep_curso.html"
    permission_required = "rep.view_curso"

    def get_context_data(self, *, object_list=None, **kwargs):
        # Con este metodo realizo los filtros de los campos
        context = super().get_context_data(**kwargs)
        context["al"] = AnioLectivo.objects.all()
        context["jo"] = GenrGeneral.objects.filter(tipo="JOR")
        return context


class ReporteProfesor(PermissionRequiredMixin, TemplateView):
    # Clase para generar el reporte de un Profesor
    template_name = "rep_profesores.html"
    permission_required = "rep.view_estudiante"

    def get_context_data(self, *, object_list=None, **kwargs):
        # Con este metodo realizo los filtros de los campos
        context = super().get_context_data(**kwargs)
        context["obj"] = Persona.objects.filter(is_empleado=True)
        return context


"""
para obtener datos del formulario
    def post(self, request, *args, **kwargs):
        # obtengo el id_persona del select
        per_id = request.POST.get("id_per")
        
        
        
        
tarea anderson, asi tengo que hacerlo

def eliminar_grupo(request):
    if request.is_ajax and request.method == "GET":
        grupo = request.GET['grupo_id']
        if grupo:
            campo = Campos.objects.filter(grupo_id=grupo).exists()
            if campo:
                estado=0
            else:
                grupo = Grupo.objects.filter(id=grupo).first()
                grupo.delete()
                estado=1
        else:
            estado=0

        return JsonResponse({'estado': estado})
    return JsonResponse({}
        
        
        
        
"""


class ReporteMatricula(PermissionRequiredMixin, TemplateView):
    # Clase para generar el reporte de matricula de un estudiante
    template_name = "rep_matricula.html"
    permission_required = "rep.view_matricula"

    def get_context_data(self, *, object_list=None, **kwargs):
        # Con este metodo realizo los filtros de los campos
        context = super().get_context_data(**kwargs)
        context["al"] = AnioLectivo.objects.all()
        context["jo"] = GenrGeneral.objects.filter(tipo="JOR")
        context["es"] = Persona.objects.filter(is_estudiante=True)
        return context







def con_jor(request):
    # Consultar jornada
    var = list()
    if request.method == "POST":
        jor_id = request.POST.get("jornada")
        j = GenrGeneral.objects.filter(idgenr_general=jor_id).first()
        if j:
            curso = CabCurso.objects.filter(id_cfg_jornada=j)
            for i in curso:
                var.append({"id": i.id_curso, "curso": i.nombre})
        return JsonResponse({"lista": var}, status=200, )


def con_cur(request):
    # Consultar curso
    var_v = list()
    if request.method == "POST":
        cur_id = request.POST.get("curso_i")
        k = CabCurso.objects.filter(id_curso=cur_id).first()
        if k:
            seccion = Aniolectivo_curso.objects.filter(id_curso=k)
            for l in seccion:
                var_v.append({"id_c": l.id_matr_anioelectivo_curso, "paralelo": l.paralelo})
        return JsonResponse({"listaa": var_v}, status=200, )
