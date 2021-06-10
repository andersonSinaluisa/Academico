from django.db import models
from django.contrib.auth.models import User
from cfg.models import GenrGeneral
from django.utils.translation import ugettext as _


class Persona(models.Model):
    """Modelo de persona, se usara para empleado, estudiante y representante"""
    id_persona = models.AutoField(primary_key=True)
    id_usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nombres = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=50, blank=False, null=False)
    identificacion = models.CharField(max_length=50, blank=False, null=False, unique=True)
    fecha_de_nacimiento = models.DateField(blank=False, null=True)
    lugar_nacimiento = models.CharField(max_length=45, blank=False, null=True)
    direccion = models.CharField(max_length=150, blank=False, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    id_cfg_genero = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, blank=False, null=True,
                                      related_name="genero", db_column='id_cfg_genero', verbose_name=_('Genero'))
    id_cfg_pais = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, blank=False, null=True,
                                    db_column='id_cfg_pais', verbose_name=_('Pais'))
    id_cfg_provincia = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="provincia",
                                         db_column='id_cfg_provincia', null=True, verbose_name=_('Provincia'))
    id_cfg_ciudad = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="ciudad",
                                      db_column='id_cfg_ciudad', null=True, verbose_name=_('Ciudad'))
    id_cfg_tipo_sangre = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="tipo_de_sangre",
                                           db_column='id_cfg_tipo_sangre', null=True, verbose_name=_('Tipo de sangre'))
    id_cfg_etnia = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="etnia",
                                     db_column='id_cfg_etnia', null=True, verbose_name=_('Etnia'))
    id_cfg_jornada = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="jornada",
                                       db_column='id_cfg_jornada', null=True, verbose_name=_('Joranda'))
    id_cfg_indigena = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="indigena",
                                        db_column='id_cfg_indigena', null=True, verbose_name=_('Etnia indigena'))
    id_cfg_idioma_ancestral = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="acestral",
                                                db_column='id_cfg_idioma_ancestral', null=True,
                                                verbose_name=_('Idioma ancestral'))
    id_cfg_categoria_migratoria = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE,
                                                    related_name="categoria_migratoria",
                                                    db_column='id_cfg_categoria_migratoria', null=True,
                                                    verbose_name=_('Categoria migratoria'))

    estado = models.ForeignKey(GenrGeneral, default=97, on_delete=models.CASCADE,
                               related_name="fk_persona_estado", db_column='estado')
    imagen = models.ImageField(upload_to='static/usuarios/', blank=False, null=True,
                               default='../../../static/img/texto-menu.pnguser_default_image.svg')
    id_cfg_estado_civil = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, blank=True, null=True,
                                            related_name="estado_civil", db_column='id_cfg_estado_civil',
                                            verbose_name=_('Estado civil'))
    fecha_ingreso = models.DateTimeField(null=True, blank=False, auto_now_add=True)
    usuario_ing = models.CharField(max_length=60, blank=False, null=False)
    terminal_ing = models.CharField(max_length=60, blank=False, null=False)

    discapacidad = models.BooleanField(blank=True, null=True, verbose_name=_('Tiene alguna discapacidad'))
    discapacidad_renal = models.BooleanField(blank=True, null=True, verbose_name=_('Padece enfermedad renal'))
    discapacidad_neurologica = models.BooleanField(blank=True, null=True,
                                                   verbose_name=_('Padece de enfermedad neurológica'))
    enfermedad_alergica = models.BooleanField(blank=True, null=True, verbose_name=_('Padece de alergias'))
    asma = models.BooleanField(blank=True, null=True, verbose_name=_('Asma'))
    epilepsia = models.BooleanField(blank=True, null=True, verbose_name=_('Epilepsia'))
    enfermedad_congenita = models.BooleanField(blank=True, null=True, verbose_name=_('Padece enfermedad cognitiva'))
    enfermedad_respiratoria = models.BooleanField(blank=True, null=True,
                                                  verbose_name=_('Padece enfermedad respiratoria'))
    atencion_psicologica = models.BooleanField(blank=True, null=True, verbose_name=_('Necesita Atención psicológica'))

    pnombres = models.CharField(max_length=45, blank=True, null=True, verbose_name=_('Nombres del padre'))
    papellidos = models.CharField(max_length=45, blank=True, null=True, verbose_name=_('Apellidos del padre'))
    pidentificacion = models.CharField(max_length=15, blank=True, null=True, verbose_name=_('Identificación del padre'))
    pdireccion = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('Dirección del padre'))
    ptelefono = models.CharField(max_length=45, blank=True, null=True, verbose_name=_('Telefono del padre'))
    pvive_con_usted = models.BooleanField(blank=True, null=True, verbose_name=_('Padre vive con el estudiante'))
    id_cfg_estado_laboralp = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="estado_laboralp",
                                               db_column='id_cfg_estado_laboralp', blank=False, null=True,
                                               verbose_name=_('Estado laboral del padre'))
    mnombres = models.CharField(max_length=45, blank=True, null=True, verbose_name=_('Nombre de la madre'))
    mapellidos = models.CharField(max_length=45, blank=True, null=True, verbose_name=_('Apellido de la madre'))
    midentificacion = models.CharField(max_length=15, blank=True, null=True,
                                       verbose_name=_('Identificación de la madre'))
    mdireccion = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('Dirección de la madre'))
    mtelefono = models.CharField(max_length=45, blank=True, null=True, verbose_name=_('Telefono de la madre'))
    mvive_con_usted = models.BooleanField(blank=True, null=True, verbose_name=_('Madre vive con el estudiante'))
    id_cfg_estado_laboralm = models.ForeignKey(GenrGeneral, blank=True, null=True, on_delete=models.CASCADE,
                                               related_name="estado_laboralm", db_column='id_cfg_estado_laboralm',
                                               verbose_name=_('Estado laboral de la madre'))
    bono_solidario = models.BooleanField(blank=True, null=True, verbose_name=_('Representante recibe bono solidario'))

    rnombres = models.CharField(max_length=45, blank=True, null=True, verbose_name=_('Nombre Representante'))
    rapellidos = models.CharField(max_length=45, blank=True, null=True, verbose_name=_('Apellido Representante'))
    rtelefono = models.CharField(max_length=45, blank=True, null=True, verbose_name=_('Telefono Representante'))
    id_cfg_tipo_identificacion = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE,
                                                   related_name="identificacion",
                                                   db_column='id_cfg_tipo_identificacion', null=True,
                                                   verbose_name=_('Tipo Identificación Representante'))
    ridentificacion = models.CharField(max_length=13, blank=True, null=True,
                                       verbose_name=_('Identificación del Representante'))
    tipo_parentesco = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Parentesco'))
    rvive_con_usted = models.BooleanField(blank=True, null=True, verbose_name=_('Representante vive con el estudiante'))
    rdireccion_trabajo = models.CharField(max_length=200, blank=True, null=True,
                                          verbose_name=_('Dirección trabajo representante'))
    rtelefono_trabajo = models.CharField(max_length=20, blank=True, null=True,
                                         verbose_name=_('Telefono trabajo representante'))
    rcorreo = models.EmailField(max_length=50, blank=False, null=True, verbose_name=_('Correo Representante'))
    rhorario_laboral = models.CharField(max_length=40, blank=True, null=True, verbose_name=_('Horario Laboral'))
    miembros_hogar = models.IntegerField(blank=True, null=True, verbose_name=_('Numero Miembros del hogar'))
    is_estudiante = models.BooleanField(null=True, verbose_name=_('Es Estudiante'))
    is_empleado = models.BooleanField(null=True, verbose_name=_('Es Empleado'))

    class Meta:
        ordering = ['nombres']

    def __str__(self):
        """función que retorna el nombre de
        un objecto Modulo

        Returns:
            [str]: [nombre del modulo]
        """
        return self.nombres + " " + self.apellidos
