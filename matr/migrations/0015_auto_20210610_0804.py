# Generated by Django 2.2.4 on 2021-06-10 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matr', '0014_auto_20210516_1858'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aniolectivo',
            options={'ordering': ['anio'], 'verbose_name': 'Año lectivo', 'verbose_name_plural': 'Año lectivo'},
        ),
    ]
