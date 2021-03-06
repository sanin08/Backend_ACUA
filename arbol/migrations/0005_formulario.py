# Generated by Django 3.0.6 on 2020-05-28 20:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('arbol', '0004_auto_20200521_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pregunta1', models.CharField(max_length=20, verbose_name='Pregunta1')),
                ('pregunta2', models.CharField(max_length=200, verbose_name='Pregunta2')),
                ('pregunta3', models.CharField(max_length=200, verbose_name='Pregunta3')),
                ('altitud', models.CharField(max_length=200, verbose_name='Altitud')),
                ('latitud', models.CharField(max_length=200, verbose_name='Latitud')),
                ('longitud', models.CharField(max_length=200, verbose_name='Longitud')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
