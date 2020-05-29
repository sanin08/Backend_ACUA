# Generated by Django 3.0.6 on 2020-05-28 23:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('arbol', '0005_formulario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('detalles', models.CharField(max_length=200, verbose_name='Correo')),
                ('puntos', models.IntegerField(verbose_name='Puntos')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('correo', models.CharField(max_length=200, verbose_name='Correo')),
                ('usuario', models.CharField(max_length=200, verbose_name='Usuario')),
                ('contraseña', models.CharField(max_length=200, verbose_name='Contraseña')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellido')),
                ('puntos', models.IntegerField(verbose_name='Puntos')),
                ('tipo', models.CharField(max_length=200, verbose_name='Tipo')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='formulario',
            name='altitud',
            field=models.IntegerField(verbose_name='Altitud'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='latitud',
            field=models.IntegerField(verbose_name='Latitud'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='longitud',
            field=models.IntegerField(verbose_name='Longitud'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='pregunta1',
            field=models.CharField(max_length=200, verbose_name='Pregunta1'),
        ),
    ]
