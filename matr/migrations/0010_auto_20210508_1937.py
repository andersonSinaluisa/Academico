# Generated by Django 2.2.4 on 2021-05-08 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matr', '0009_auto_20210508_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallemateriacurso',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
