# Generated by Django 4.0.1 on 2022-07-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Objetivos', '0002_objeto_autor_principal_alter_objeto_archivo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objeto',
            name='precio',
        ),
        migrations.AlterField(
            model_name='objeto',
            name='estatus',
            field=models.CharField(max_length=45),
        ),
    ]
