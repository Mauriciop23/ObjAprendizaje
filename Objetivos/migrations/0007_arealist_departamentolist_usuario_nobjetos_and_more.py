# Generated by Django 4.1.1 on 2022-09-08 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Objetivos', '0006_objeto_descripcion_otro_alter_objeto_archivo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaList',
            fields=[
                ('idarea', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'arealist',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DepartamentoList',
            fields=[
                ('iddepartamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'departamentolist',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='usuario',
            name='nobjetos',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Numero de objetos'),
        ),
        migrations.DeleteModel(
            name='autor',
        ),
    ]
