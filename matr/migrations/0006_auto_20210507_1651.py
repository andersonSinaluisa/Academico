# Generated by Django 2.2.4 on 2021-05-07 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matr', '0005_auto_20210507_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aniolectivo_curso',
            old_name='id_estado_gnral',
            new_name='estado',
        ),
    ]
