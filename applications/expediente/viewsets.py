from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
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
        #Valida que la información sea correcta
        serializer.is_valid(raise_exception=True)
        
        # exp = Expediente.objects.create(
        #     no_radicacion = serializer.validated_data['no_radicacion'],
        #     documento_final = serializer.validated_data['documento_final'],
        #     fecha_radicacion = serializer.validated_data['fecha_radicacion'],
        #     fecha_expedicion = serializer.validated_data['fecha_expedicion'],
        #     fecha_ejecutoria = serializer.validated_data['fecha_ejecutoria'],
        #     fecha_inicio = serializer.validated_data['fecha_inicio'],
        #     fecha_final = serializer.validated_data['fecha_final'],
        #     tipo_acto_administrativo = serializer.validated_data['tipo_acto_administrativo.id'],
        #     usuario= serializer.validated_data['usuario.pk'],
        # )
        # inf = InformacionGeneral.objects.create(
        #     no_radicacion = exp.id,
        #     tramite = serializer.validated_data['tramite'],
        #     alcaldia = serializer.validated_data['alcaldia'],
        #     urbanizacion = serializer.validated_data['urbanizacion']
        # )
        dicc = serializer.data['tipo_acto_administrativo']
        print(dicc)
        return  Response({
            'ok': 'ok',
            'data': {
                'hola': 'mundo',
            }
        })

    def retrieve(self, request, pk=None):
        venta = get_object_or_404(Expediente.objects.all(), pk=pk)
        serializer = ExpedienteSerializerViewset(venta)
        return Response(serializer.data)