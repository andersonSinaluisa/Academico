from django.db import models
from django.contrib.auth.models import User
from cfg.models import GenrGeneral


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
                                      related_name="genero", db_column='id_cfg_genero')
    id_cfg_pais = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, blank=False, null=True,
                                    db_column='id_cfg_pais')
    id_cfg_provincia = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="provincia",
                                         db_column='id_cfg_provincia', null=True)
    id_cfg_ciudad = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="ciudad",
                                      db_column='id_cfg_ciudad', null=True)
    id_cfg_tipo_sangre = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="tipo_de_sangre",
                                           db_column='id_cfg_tipo_sangre', null=True)
    id_cfg_etnia = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="etnia",
                                     db_column='id_cfg_etnia', null=True)
    id_cfg_jornada = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="jornada",
                                       db_column='id_cfg_jornada', null=True)
    id_cfg_indigena = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="indigena",
                                        db_column='id_cfg_indigena', null=True)
    id_cfg_idioma_ancestral = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="acestral",
                                                db_column='id_cfg_idioma_ancestral', null=True)
    id_cfg_categoria_migratoria = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE,
                                                    related_name="categoria_migratoria",
                                                    db_column='id_cfg_categoria_migratoria', null=True)

    estado = models.ForeignKey(GenrGeneral, default=97, on_delete=models.CASCADE,
                               related_name="fk_persona_estado", db_column='estado')
    imagen = models.ImageField(upload_to='static/usuarios/', blank=False, null=True,
                               default='../../../static/img/texto-menu.pnguser_default_image.svg')
    id_cfg_estado_civil = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, blank=True, null=True,
                                            related_name="estado_civil", db_column='id_cfg_estado_civil')
    fecha_ingreso = models.DateTimeField(null=True, blank=False, auto_now_add=True)
    usuario_ing = models.CharField(max_length=60, blank=False, null=False)
    terminal_ing = models.CharField(max_length=60, blank=False, null=False)

    discapacidad = models.BooleanField(blank=True, null=True)
    discapacidad_renal = models.BooleanField(blank=True, null=True)
    discapacidad_neurologica = models.BooleanField(blank=True, null=True)
    enfermedad_alergica = models.BooleanField(blank=True, null=True)
    asma = models.BooleanField(blank=True, null=True)
    epilepsia = models.BooleanField(blank=True, null=True)
    enfermedad_congenita = models.BooleanField(blank=True, null=True)
    enfermedad_respiratoria = models.BooleanField(blank=True, null=True)
    atencion_psicologica = models.BooleanField(blank=True, null=True)
    id_cfg_tipo_usuario = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, blank=False, null=False,
                                            default=19, related_name="persona_tipo_usuario",
                                            db_column='id_cfg_tipo_usuario')

    pnombres = models.CharField(max_length=45, blank=True, null=True)
    papellidos = models.CharField(max_length=45, blank=True, null=True)
    pidentificacion = models.CharField(max_length=15, blank=True, null=True)
    pdireccion = models.CharField(max_length=50, blank=True, null=True)
    ptelefono = models.CharField(max_length=45, blank=True, null=True)
    pvive_con_usted = models.BooleanField(blank=True, null=True)
    id_cfg_estado_laboralp = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE, related_name="estado_laboralp",
                                               db_column='id_cfg_estado_laboralp', blank=False, null=True)
    mnombres = models.CharField(max_length=45, blank=True, null=True)
    mapellidos = models.CharField(max_length=45, blank=True, null=True)
    midentificacion = models.CharField(max_length=15, blank=True, null=True)
    mdireccion = models.CharField(max_length=50, blank=True, null=True)
    mtelefono = models.CharField(max_length=45, blank=True, null=True)
    mvive_con_usted = models.BooleanField(blank=True, null=True)
    id_cfg_estado_laboralm = models.ForeignKey(GenrGeneral, blank=True, null=True, on_delete=models.CASCADE,
                                               related_name="estado_laboralm", db_column='id_cfg_estado_laboralm')
    bono_solidario = models.BooleanField(blank=True, null=True)

    rnombres = models.CharField(max_length=45, blank=True, null=True, default="nombre representante")
    rapellidos = models.CharField(max_length=45, blank=True, null=True, default="apellido representante")
    rtelefono = models.CharField(max_length=45, blank=True, null=True)
    id_cfg_tipo_identificacion = models.ForeignKey(GenrGeneral, on_delete=models.CASCADE,
                                                   related_name="identificacion",
                                                   db_column='id_cfg_tipo_identificacion', null=True)
    ridentificacion = models.CharField(max_length=13, blank=True, null=True)
    tipo_parentesco = models.CharField(max_length=200, blank=True, null=True)
    rvive_con_usted = models.BooleanField(blank=True, null=True)
    rdireccion_trabajo = models.CharField(max_length=200, blank=True, null=True)
    rtelefono_trabajo = models.CharField(max_length=20, blank=True, null=True)
    rcorreo = models.EmailField(max_length=50, blank=False, null=True)
    rhorario_laboral = models.CharField(max_length=40, blank=True, null=True)
    miembros_hogar = models.IntegerField(blank=True, null=True)
    is_estudiante = models.BooleanField(null=True)
    is_empleado = models.BooleanField(null=True)
    is_representante = models.BooleanField(null=True)
