# Generated by Django 2.2.4 on 2021-05-08 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matr', '0006_auto_20210507_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id_materia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('estado', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Materia',
            },
        ),
        migrations.AlterField(
            model_name='cabcurso',
            name='id_cfg_jornada',
            field=models.ForeignKey(db_column='id_cfg_jornada', on_delete=django.db.models.deletion.CASCADE, related_name='fk_cabcurso_jornada', to='cfg.GenrGeneral', verbose_name='Jornada'),
        ),
    ]
