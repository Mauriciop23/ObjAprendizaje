# Generated by Django 4.1.1 on 2022-09-08 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Objetivos', '0007_arealist_departamentolist_usuario_nobjetos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arealist',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='departamentolist',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]
