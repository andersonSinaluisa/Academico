from django.urls import path
from rep.views import *

urlpatterns = [
    path("reporte-cursos/", ReporteCurso.as_view(), name="reporte_cursos"),
    path("reporte-profesores/", ReporteProfesor.as_view(), name="reporte_profesores"),
    path("reporte-matricula/", ReporteMatricula.as_view(), name="reporte_matricula"),
    # url de metodos para consultar cursos y secciones en matricula y estudiantes
    path("consultar-cursos/", con_jor, name="consultar_cursos"),
    path("consultar-secciones/", con_cur, name="consultar_secciones"),
]
