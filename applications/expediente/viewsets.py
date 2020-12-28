from rest_framework import viewsets, status
from rest_framework.response import Response
from applications.users.backends import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from applications.utilidades.models import (
    TipoActoAdministrativo, 
    Tramite, 
    Alcaldia, 
    Modalidades
)
from .models import *
from .serializers import (
    ExpedienteCreacion,
    ActuacionPosteriorSerializer,
    DireccionesSerializer,
    FotosSerializer
)

class ExpedienteViewset(viewsets.ViewSet):

    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        # queryset = Expediente.objects.informacion_expediente()
        # serializer = ExpedienteCreacion(queryset, many=True)
        return Response({
            '', ''
        })

    def create(self, request):

        serializer =ExpedienteCreacion(data=request.data)
        serializer.is_valid(raise_exception=True)

        exp = Expediente.objects.crear_o_actualizar_expediente(serializer.validated_data)
        inf = InformacionGeneral.objects.crear_o_actualizar_informacion(exp, serializer.validated_data)

        content = {
            'message': 'ok',
            'id': exp.id,
        }

        return  Response(content, status = status.HTTP_201_CREATED)

    def update(self, request, pk=None):

        serializer =ExpedienteCreacion(data=request.data)
        serializer.is_valid(raise_exception=True)

        exp = Expediente.objects.crear_o_actualizar_expediente(serializer.validated_data)
        inf = InformacionGeneral.objects.crear_o_actualizar_informacion(exp, serializer.validated_data)

        content = {
            'message': 'ok',
            'id': exp.id,
        }

        return  Response(content, status = status.HTTP_200_OK)

        

    def retrieve(self, request, pk=None):
        expediente = get_object_or_404(Expediente.objects.informacion_expediente(), pk=pk)
        serializer = ExpedienteCreacion(expediente)
        return Response(serializer.data)   


class ActuacionesPosterioresViewset(viewsets.ModelViewSet):

    serializer_class = ActuacionPosteriorSerializer
    queryset = ActuacionPosterior.objects.all()


class DireccionesViewset(viewsets.ModelViewSet):

    serializer_class = DireccionesSerializer
    queryset = Direcciones.objects.all()


class FotosViewset(viewsets.ModelViewSet):

    serializer_class = FotosSerializer
    queryset = Fotos.objects.all()