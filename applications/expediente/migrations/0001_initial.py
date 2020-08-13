# Generated by Django 3.0.5 on 2020-08-13 16:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utilidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActuacionPosterior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('acto_administrativo', models.CharField(max_length=20, verbose_name='Acto administrativo')),
                ('fecha_expedicion', models.DateField(blank=True, null=True, verbose_name='Fecha de expedición')),
                ('fecha_ejecutoria', models.DateField(blank=True, null=True, verbose_name='Fecha ejecutoria')),
            ],
            options={
                'verbose_name': 'Actuación posterior',
                'verbose_name_plural': 'Actuaciones posteriores',
                'ordering': ['-no_radicacion'],
            },
        ),
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('direccion', models.CharField(blank=True, max_length=50, verbose_name='Direccion')),
                ('chip', models.CharField(blank=True, max_length=50, verbose_name='CHIP')),
                ('matricula_inmobiliaria', models.CharField(blank=True, max_length=50, verbose_name='Matrícula inmobiliaría')),
                ('anterior', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Dirección',
                'verbose_name_plural': 'Direcciones',
                'ordering': ['-no_radicacion'],
            },
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('no_radicacion', models.CharField(max_length=20, unique=True, verbose_name='Expediente')),
                ('documento_final', models.CharField(max_length=15, verbose_name='Documento final')),
                ('fecha_radicacion', models.DateField(blank=True, null=True, verbose_name='Fecha de radicación')),
                ('fecha_expedicion', models.DateField(blank=True, null=True, verbose_name='Fecha de expedición')),
                ('fecha_ejecutoria', models.DateField(blank=True, null=True, verbose_name='Fecha ejecutoria')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha de inicio')),
                ('fecha_final', models.DateField(blank=True, null=True, verbose_name='Fecha final')),
                ('tipo_acto_administrativo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='utilidades.TipoActoAdministrativo')),
            ],
            options={
                'verbose_name': 'Expediente',
                'verbose_name_plural': 'Expedientes',
                'ordering': ['-no_radicacion'],
            },
        ),
        migrations.CreateModel(
            name='InformacionGeneral',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('no_radicacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='expediente.Expediente')),
                ('urbanizacion', models.CharField(blank=True, max_length=30, verbose_name='Urbanización')),
            ],
            options={
                'verbose_name': 'Información General',
                'verbose_name_plural': 'Información General',
                'ordering': ['-no_radicacion'],
            },
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('folios', models.CharField(max_length=30, verbose_name='Folios')),
                ('no_radicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.Expediente')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
                'ordering': ['-no_radicacion'],
            },
        ),
    ]
