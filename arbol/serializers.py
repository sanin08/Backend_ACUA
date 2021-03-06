from rest_framework import serializers
from .models import Arbol
from .models import Formulario
from .models import Usuario
from .models import Tarea

class ArbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arbol
        fields = ('id', 'tipo', 'carac','direction','cupo')

class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Formulario
        fields= ('id','pregunta1','pregunta2','pregunta3','altitud','latitud')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields= ('id','correo','usuario','contraseña','nombre','apellido','puntos','tipo')

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tarea
        fields= ('id','detalles','puntos')


