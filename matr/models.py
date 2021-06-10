from django.db import models
from django.utils.translation import ugettext as _

from cfg.models import GenrGeneral
from mant.models import Persona


class AnioLectivo(models.Model):
    id_anio_lectivo = models.AutoField(primary_key=True)
    anio = models.IntegerField(blank=False, null=False)
    ciclo = models.IntegerField(blank=False, null=False)
    fecha_incio_ciclo = models.DateField(blank=False, null=False)
    fecha_fin_ciclo = models.DateField(blank=False, null=False)
    estado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Año lectivo'
        verbose_name_plural = 'Año lectivo'
        ordering = ['anio']

    def __str__(self):
        return str(self.anio)


class CabCurso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=10)
    id_cfg_regimen = models.ForeignKey(GenrGeneral, default=97, on_delete=models.CASCADE, blank=False,
                                       related_name='fk_cabcurso_regimen', null=False, db_column='id_cfg_regimen',
                                       verbose_name=_("Regimen"))
    id_cfg_modalidad = models.ForeignKey(GenrGeneral, default=97, on_delete=models.CASCADE, blank=False, null=False,
                                         related_name='fk_cabcurso_modalidad', db_column='id_cfg_modalidad',
                                         verbose_name=_("Modalidad"))
    id_cfg_tipo_edu = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, blank=False, null=False,
                                        related_name='fk_materiaprof_tipoedu', db_column='id_cfg_tipo_educacion',
                                        verbose_name=_("Tipo de educación"))
    id_cfg_formacion = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, blank=False, null=False,
                                         related_name="fk_cabcurso_formacion", db_column='id_cfg_formacion',
                                         verbose_name=_("Formación"))
    id_cfg_jornada = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, blank=False, null=False,
                                       related_name="fk_cabcurso_jornada", db_column='id_cfg_jornada',
                                       verbose_name=_("Jornada"))
    cupo = models.IntegerField()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nombre + " " + self.id_cfg_formacion.nombre


class Aniolectivo_curso(models.Model):
    id_matr_anioelectivo_curso = models.AutoField(primary_key=True)
    id_anio_electivo = models.ForeignKey(AnioLectivo, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(CabCurso, on_delete=models.CASCADE, blank=False, null=False, db_column='id_curso')
    paralelo = models.CharField(max_length=2)
    cupos = models.IntegerField(default=45)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Año Lectivo Curso'

    def __str__(self):
        return self.id_curso.nombre + " " + self.id_curso.id_cfg_formacion.nombre + " " + self.paralelo + " " + str(
            self.id_anio_electivo.anio)


class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    estado = models.BooleanField()

    class Meta:
        verbose_name = 'Materia'

    def __str__(self):
        return self.nombre


class DetalleMateriaCurso(models.Model):
    id_detalle_materia_curso = models.AutoField(primary_key=True)
    id_matr_anio_lectivo_curso = models.ForeignKey(Aniolectivo_curso, on_delete=models.CASCADE, blank=False, null=False,
                                                   related_name="fk_detallemateriacurso_aniolectivocurso",
                                                   db_column='id_matr_aniolectivo_curso')
    total_horas = models.DecimalField(decimal_places=2, max_digits=4)
    estado = models.BooleanField(default=True)
    id_materia = models.ForeignKey(Materia, blank=False, default=24, related_name="fk_detallemateriacurso_materias",
                                   db_column='id_materia', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Detalle Materia Curso'
        verbose_name_plural = 'Detalle Materia Curso'


class MatriculacionEstudiante(models.Model):
    id_matriculacion_estudiante = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False,
                                      related_name="fk_matriculacionestudiante_estudiante")
    id_matr_anioelectivo_curso = models.ForeignKey(Aniolectivo_curso, on_delete=models.CASCADE, blank=True, null=True,
                                                   related_name="fk_matriculacionestudiante_aniolectivo_curso")
    estado = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, default=97,
                               related_name="fk_matriculacionestudiante_estado", db_column='estado')
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    usuario_ing = models.CharField(max_length=45, blank=True, null=True)
    terminal_ing = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        verbose_name = 'Matriculacion estudiante'
        verbose_name_plural = 'Matriculacion estudiante'

    def __str__(self):
        return self.id_estudiante.id_persona.nombres + " " + self.id_estudiante.id_persona.apellidos


class Materia_profesor(models.Model):
    id_materia_profesor = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False,
                                    related_name='fk_materiaprof_empleado', db_column='id_empleado')
    id_detalle_materia_curso = models.ForeignKey(DetalleMateriaCurso, on_delete=models.CASCADE,
                                                 related_name="fk_materia_profesor", null=False, blank=False)
    hora_inicio = models.TimeField(verbose_name=_("Hora de inicio"))
    hora_fin = models.TimeField(verbose_name=_("Hora fin"))
    dia_semana = models.IntegerField()

    class Meta:
        verbose_name = 'Materia profesor'
        verbose_name_plural = 'Materia profesores'
