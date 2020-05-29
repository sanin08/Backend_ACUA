from django.db import models
import uuid

class Arbol(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    carac = models.CharField(verbose_name='caracteristica', max_length=200)
    direction = models.CharField(verbose_name='direccion', max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Formulario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pregunta1 = models.CharField(verbose_name='Pregunta1', max_length=200)
    pregunta2 = models.CharField(verbose_name='Pregunta2', max_length=200)
    pregunta3 = models.CharField(verbose_name='Pregunta3', max_length=200)
    altitud = models.IntegerField(verbose_name='Altitud')
    latitud = models.IntegerField(verbose_name='Latitud')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    correo = models.CharField(verbose_name='Correo', max_length=200)
    usuario = models.CharField(verbose_name='Usuario', max_length=200)
    contraseña = models.CharField(verbose_name='Contraseña', max_length=200)
    nombre = models.CharField(verbose_name='Nombre', max_length=200)
    apellido = models.CharField(verbose_name='Apellido', max_length=200)
    puntos = models.IntegerField(verbose_name='Puntos')
    tipo = models.CharField(verbose_name='Tipo', max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Tarea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    detalles = models.CharField(verbose_name='Correo', max_length=200)
    puntos = models.IntegerField(verbose_name='Puntos')