from rest_framework import viewsets
from .models import Arbol
from .serializers import ArbolSerializer

class ArbolViewSet(viewsets.ModelViewSet):
    queryset = Arbol.objects.all().order_by('-created')
    serializer_class =ArbolSerializer

from rest_framework import viewsets
from .models import Formulario
from .serializers import FormularioSerializer

class FormularioViewSet(viewsets.ModelViewSet):
    queryset = Formulario.objects.all().order_by('-created')
    serializer_class =FormularioSerializer

from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('-created')
    serializer_class =UsuarioSerializer

from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all().order_by('-created')
    serializer_class =TareaSerializer