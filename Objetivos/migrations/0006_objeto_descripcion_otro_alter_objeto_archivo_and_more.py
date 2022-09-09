# Generated by Django 4.1.1 on 2022-09-07 21:14

import Objetivos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Objetivos', '0005_objeto_coautores'),
    ]

    operations = [
        migrations.AddField(
            model_name='objeto',
            name='descripcion_otro',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='objeto',
            name='archivo',
            field=models.FileField(blank=True, max_length=240, null=True, upload_to=Objetivos.models.objeto_directory_path),
        ),
        migrations.AlterField(
            model_name='objeto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]