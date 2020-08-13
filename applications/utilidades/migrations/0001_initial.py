# Generated by Django 3.0.5 on 2020-08-11 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alcaldia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_alcaldia', models.IntegerField(unique=True)),
                ('alcaldia', models.CharField(max_length=20, unique=True, verbose_name='Alcaldía')),
            ],
            options={
                'verbose_name': 'Alcaldía',
                'verbose_name_plural': 'Alcaldías',
                'ordering': ['alcaldia'],
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=60, unique=True, verbose_name='Documento')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
                'ordering': ['documento'],
            },
        ),
        migrations.CreateModel(
            name='Modalidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_modalidad', models.IntegerField(verbose_name='Código de modalidad')),
                ('modalidad', models.CharField(max_length=20, verbose_name='Código de modalidad')),
            ],
            options={
                'verbose_name': 'Modalidad',
                'verbose_name_plural': 'Modalidades',
                'ordering': ['modalidad'],
            },
        ),
        migrations.CreateModel(
            name='TipoActoAdministrativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_acto_administrativo', models.IntegerField(unique=True)),
                ('tipo_acto_administrativo', models.CharField(max_length=20, unique=True, verbose_name='Tipo de acto administrativo')),
            ],
            options={
                'verbose_name': 'Tipo de acto administrativo',
                'verbose_name_plural': 'Tipos de actos administrativos',
                'ordering': ['tipo_acto_administrativo'],
            },
        ),
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_tramite', models.IntegerField(unique=True)),
                ('tramite', models.CharField(max_length=70, unique=True, verbose_name='Trámite')),
            ],
            options={
                'verbose_name': 'Trámite',
                'verbose_name_plural': 'Trámites',
                'ordering': ['tramite'],
            },
        ),
    ]