# Generated by Django 2.2.4 on 2021-05-07 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matr', '0003_auto_20210507_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aniolectivo_curso',
            name='id_estado_gnral',
            field=models.BooleanField(default=True),
        ),
    ]
