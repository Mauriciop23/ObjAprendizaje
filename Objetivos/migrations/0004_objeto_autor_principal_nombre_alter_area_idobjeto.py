# Generated by Django 4.0.1 on 2022-08-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Objetivos', '0003_remove_objeto_precio_alter_objeto_estatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='objeto',
            name='autor_principal_nombre',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='idobjeto',
            field=models.CharField(max_length=45),
        ),
    ]
