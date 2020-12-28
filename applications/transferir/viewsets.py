from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from applications.utilidades.models import Documento
from .models import *
from .serializers import *

class CajasViewset(viewsets.ModelViewSet):

    serializer_class = CajaSerializer
    queryset = Caja.objects.all()

class CarpetaViewset(viewsets.ModelViewSet):

    serializer_class = CarpetaSerializer
    queryset = Carpeta.objects.all()

class DocumentosViewset(viewsets.ModelViewSet):

    serializer_class = DocumentosSerializer
    queryset = Document.objects.all()