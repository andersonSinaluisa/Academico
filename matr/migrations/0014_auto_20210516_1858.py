# Generated by Django 2.2.4 on 2021-05-16 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matr', '0013_auto_20210516_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallemateriacurso',
            name='total_horas',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
