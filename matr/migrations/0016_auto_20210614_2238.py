# Generated by Django 2.2.4 on 2021-06-14 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matr', '0015_auto_20210610_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallemateriacurso',
            name='total_horas',
            field=models.CharField(max_length=9),
        ),
    ]