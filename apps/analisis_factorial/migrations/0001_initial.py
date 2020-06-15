# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-31 13:02
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('completado', models.BooleanField(default=False)),
                ('numero_componenentes', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('rotacion', models.CharField(choices=[('variamax', 'Variamax'), ('promax', 'Promax'), ('oblimin', 'Oblimin'), ('oblimax', 'Oblimax'), ('quartimin', 'Quartimin'), ('quartimax', 'Quartimax'), ('equamax', 'Equamax')], default='variamax', max_length=10)),
                ('archivo_datos', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ProyectoAnalisisFactorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('objetivos', models.TextField(blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('fecha_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_final', models.DateTimeField(default=django.utils.timezone.now)),
                ('estado', models.BooleanField(default=False)),
                ('moderador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='analisis_factorial_moderador', to=settings.AUTH_USER_MODEL, verbose_name='moderador_analisis_factorial')),
            ],
        ),
        migrations.AddField(
            model_name='estudio',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analisis_factorial_estudio', to='analisis_factorial.ProyectoAnalisisFactorial', verbose_name='estudio_analisis_factorial'),
        ),
    ]