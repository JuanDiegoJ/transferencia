from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from applications.utilidades.models import (
    TipoActoAdministrativo, 
    Tramite, 
    Alcaldia, 
    Modalidades
)
from .models import Expediente, InformacionGeneral
from .serializers import (
    ExpedienteSerializerViewset,
    ExpedienteCreacion
)

class ExpedienteViewset(viewsets.ViewSet):

    def list(self, request, *args, **kwargs):
        queryset = Expediente.objects.all()
        serializer = ExpedienteSerializerViewset(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):

        serializer =ExpedienteCreacion(data=request.data)
        serializer.is_valid(raise_exception=True)

        exp = Expediente.objects.create(
            no_radicacion = serializer.validated_data['no_radicacion'],
            documento_final = serializer.validated_data['documento_final'],
            fecha_radicacion = serializer.validated_data['fecha_radicacion'],
            fecha_expedicion = serializer.validated_data['fecha_expedicion'],
            fecha_ejecutoria = serializer.validated_data['fecha_ejecutoria'],
            fecha_inicio = serializer.validated_data['fecha_inicio'],
            fecha_final = serializer.validated_data['fecha_final'],
            tipo_acto_administrativo = TipoActoAdministrativo.objects.filter(id=serializer.validated_data['tipo_acto_administrativo']).get(),
            #usuario = self.request.user
        )

        inf = InformacionGeneral.objects.create(
            no_radicacion = exp,
            tramite = Tramite.objects.filter(id=serializer.validated_data['tramite']).get(),
            alcaldia = Alcaldia.objects.filter(id=serializer.validated_data['alcaldia']).get(),
            urbanizacion = serializer.validated_data['urbanizacion']
        )

        modalidades = Modalidades.objects.filter(
            id__in = serializer.validated_data['modalidades']
        )
        print(modalidades)

        for modalidad in modalidades:
            inf.modalidades.add(modalidad)

        return  Response({
            'ok': 'ok',
            'data': exp.id
        })

    def retrieve(self, request, pk=None):
        expediente = get_object_or_404(Expediente.objects.all(), pk=pk)
        serializer = ExpedienteSerializerViewset(expediente)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        expediente = get_object_or_404(Expediente.objects.all(), pk=pk)
        serializer = ExpedienteCreacion(expediente)
        print(expediente)
        return Response(serializer.data)