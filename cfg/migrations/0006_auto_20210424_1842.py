# Generated by Django 2.2.4 on 2021-04-24 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfg', '0005_auto_20210424_0106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genrgeneral',
            options={'verbose_name': 'Lista_General', 'verbose_name_plural': 'Listas_General'},
        ),
        migrations.AlterModelOptions(
            name='genrhistorial',
            options={'verbose_name': 'Historial', 'verbose_name_plural': 'Historiales'},
        ),
        migrations.AlterModelOptions(
            name='mensajepantalla',
            options={'verbose_name': 'Mensaje Pantalla', 'verbose_name_plural': 'Mensajes Pantallas'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Menu', 'verbose_name_plural': 'Menus'},
        ),
        migrations.AlterModelOptions(
            name='modulo',
            options={'ordering': ['codigo'], 'verbose_name': 'Modulo', 'verbose_name_plural': 'Modulos'},
        ),
    ]
