# Generated by Django 2.2.4 on 2021-05-05 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cfg', '0006_auto_20210424_1842'),
        ('mant', '0005_remove_persona_is_representante'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnioLectivo',
            fields=[
                ('id_anio_lectivo', models.AutoField(primary_key=True, serialize=False)),
                ('anio', models.IntegerField(unique=True)),
                ('ciclo', models.IntegerField(unique=True)),
                ('fecha_incio_ciclo', models.DateField()),
                ('fecha_fin_ciclo', models.DateField()),
                ('id_cfg_estado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': ('Año lectivo',),
                'verbose_name_plural': ('Año lectivo',),
            },
        ),
        migrations.CreateModel(
            name='Aniolectivo_curso',
            fields=[
                ('id_matr_anioelectivo_curso', models.AutoField(primary_key=True, serialize=False)),
                ('paralelo', models.CharField(max_length=2)),
                ('id_anio_electivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matr.AnioLectivo')),
            ],
            options={
                'verbose_name': 'Año Lectivo Curso',
            },
        ),
        migrations.CreateModel(
            name='DetalleMateriaCurso',
            fields=[
                ('id_detalle_materia_curso', models.AutoField(primary_key=True, serialize=False)),
                ('total_horas', models.IntegerField(default=1)),
                ('estado', models.ForeignKey(db_column='estado', default='97', on_delete=django.db.models.deletion.CASCADE, related_name='fk_detallemateriacurso_estado', to='cfg.GenrGeneral')),
                ('id_cfg_materias', models.ForeignKey(db_column='id_cfg_materias', default=24, on_delete=django.db.models.deletion.CASCADE, related_name='fk_detallemateriacurso_materias', to='cfg.GenrGeneral')),
                ('id_matr_anio_lectivo_curso', models.ForeignKey(db_column='id_matr_aniolectivo_curso', on_delete=django.db.models.deletion.CASCADE, related_name='fk_detallemateriacurso_aniolectivocurso', to='matr.Aniolectivo_curso')),
            ],
            options={
                'verbose_name': 'Detalle Materia Curso',
                'verbose_name_plural': 'Detalle Materia Curso',
            },
        ),
        migrations.CreateModel(
            name='MatriculacionEstudiante',
            fields=[
                ('id_matriculacion_estudiante', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_ingreso', models.DateTimeField(blank=True, null=True)),
                ('usuario_ing', models.CharField(blank=True, max_length=45, null=True)),
                ('terminal_ing', models.CharField(blank=True, max_length=45, null=True)),
                ('estado', models.ForeignKey(db_column='estado', default=97, on_delete=django.db.models.deletion.CASCADE, related_name='fk_matriculacionestudiante_estado', to='cfg.GenrGeneral')),
                ('id_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_matriculacionestudiante_estudiante', to='mant.Persona')),
                ('id_matr_anioelectivo_curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_matriculacionestudiante_aniolectivo_curso', to='matr.Aniolectivo_curso')),
            ],
            options={
                'verbose_name': 'Matriculacion estudiante',
                'verbose_name_plural': 'Matriculacion estudiante',
            },
        ),
        migrations.CreateModel(
            name='Materia_profesor',
            fields=[
                ('id_materia_profesor', models.AutoField(primary_key=True, serialize=False)),
                ('id_detalle_materia_curso', models.ManyToManyField(db_table='matr_profesor_materiacurso', related_name='fk_materia_profesor', to='matr.DetalleMateriaCurso')),
                ('id_empleado', models.ForeignKey(db_column='id_empleado', on_delete=django.db.models.deletion.CASCADE, related_name='fk_materiaprof_empleado', to='mant.Persona')),
            ],
            options={
                'verbose_name': 'Materia profesor',
                'verbose_name_plural': 'Materia profesores',
            },
        ),
        migrations.CreateModel(
            name='CabCurso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=10)),
                ('cupo', models.IntegerField()),
                ('id_cfg_curso', models.ForeignKey(db_column='id_cfg_curso', default=97, on_delete=django.db.models.deletion.CASCADE, related_name='fk_cabcurso_curso', to='cfg.GenrGeneral')),
                ('id_cfg_formacion', models.ForeignKey(db_column='id_cfg_formacion', on_delete=django.db.models.deletion.CASCADE, related_name='fk_cabcurso_formacion', to='cfg.GenrGeneral')),
                ('id_cfg_jornada', models.ForeignKey(db_column='id_cfg_jornada', on_delete=django.db.models.deletion.CASCADE, related_name='fk_cabcurso_jornada', to='cfg.GenrGeneral')),
                ('id_cfg_modalidad', models.ForeignKey(db_column='id_cfg_modalidad', default=97, on_delete=django.db.models.deletion.CASCADE, related_name='fk_cabcurso_modalidad', to='cfg.GenrGeneral')),
                ('id_cfg_regimen', models.ForeignKey(db_column='id_cfg_regimen', default=97, on_delete=django.db.models.deletion.CASCADE, related_name='fk_cabcurso_regimen', to='cfg.GenrGeneral')),
                ('id_cfg_tipo_edu', models.ForeignKey(db_column='id_cfg_tipo_educacion', on_delete=django.db.models.deletion.CASCADE, related_name='fk_materiaprof_tipoedu', to='cfg.GenrGeneral')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.AddField(
            model_name='aniolectivo_curso',
            name='id_curso',
            field=models.ForeignKey(db_column='id_curso', on_delete=django.db.models.deletion.CASCADE, to='matr.CabCurso'),
        ),
        migrations.AddField(
            model_name='aniolectivo_curso',
            name='id_estado_gnral',
            field=models.ForeignKey(db_column='estado', default=97, on_delete=django.db.models.deletion.CASCADE, to='cfg.GenrGeneral'),
        ),
    ]
