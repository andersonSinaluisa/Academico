# Generated by Django 2.2.4 on 2021-04-22 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfg', '0002_modulo_icono'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='orden',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
