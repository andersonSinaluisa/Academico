from django.urls import path
from matr.views import AnioLectivoListar, AnioLectivoCrear, AnioLectivoEditar,\
    CabCursoLista, CabCursoCrear, MateriasLista, MateriasCrear, MateriasEditar,\
    CabCursoEditar, CursoDetalle, AsignacionMateriaProfesor, AsignacionesCrear,\
    conultar_materias_paralelo, guardar_horario_profesor

urlpatterns = [
    path('anios-lectivo/', AnioLectivoListar.as_view(), name="anios_lectivo"),
    path("crear-anio-lectivo/", AnioLectivoCrear.as_view(),
         name="crear_anio_lectivo"),
    path("editar-anio-lectivo/<int:pk>",
         AnioLectivoEditar.as_view(), name="editar_anio_lectivo"),
    path("cursos/", CabCursoLista.as_view(), name="cursos"),
    path("crear-curso/", CabCursoCrear.as_view(), name="crear_curso"),
    path("editar-curso/<int:pk>", CabCursoEditar.as_view(), name="editar_curso"),
    path("materias/", MateriasLista.as_view(), name="materias"),
    path("crear-materia/", MateriasCrear.as_view(), name="crear_materia"),
    path("editar-materia/<int:pk>",
         MateriasEditar.as_view(), name="editar_materia"),
    path("curso-ver/<int:pk>", CursoDetalle.as_view(), name="curso_ver"),
    path("materias-profesor/", AsignacionMateriaProfesor.as_view(),
         name="materias_profesor"),
    path("asignar-materia-profesor/<int:pk>",
         AsignacionesCrear.as_view(), name="asignar_materia_profesor"),
    path("consultar-materia/", conultar_materias_paralelo, name="consultar_materia"),
    path("profesor-materia/",guardar_horario_profesor,name="profesor_materia")
]
