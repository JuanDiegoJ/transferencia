from rest_framework import serializers

from .models import Expediente, InformacionGeneral
from applications.utilidades.serializers import TipoActoAdministrativoSerializer, TramiteSerializer
from applications.users.serializers import UserSerializer


class InformacionGeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = InformacionGeneral
        fields = ('__all__')


class ExpedienteSerializerViewset(serializers.Serializer):

    id = serializers.IntegerField()
    no_radicacion = serializers.CharField()
    documento_final = serializers.CharField()
    fecha_radicacion = serializers.DateField()
    fecha_expedicion = serializers.DateField()
    fecha_ejecutoria = serializers.DateField()
    fecha_inicio = serializers.DateField()
    fecha_final = serializers.DateField()
    tipo_acto_administrativo = TipoActoAdministrativoSerializer()
    usuario = UserSerializer()
    informacion = serializers.SerializerMethodField()

    def get_informacion(self, obj):
        query = InformacionGeneral.objects.filter(
            no_radicacion = obj.id
        )
        print(query)
        productos_serializados = InformacionGeneralSerializer(query, many=True).data
        print(productos_serializados)
        return productos_serializados


class ExpedienteCreacion(serializers.Serializer):

    no_radicacion = serializers.CharField()
    documento_final = serializers.CharField()
    fecha_radicacion = serializers.DateField()
    fecha_expedicion = serializers.DateField()
    fecha_ejecutoria = serializers.DateField()
    fecha_inicio = serializers.DateField()
    fecha_final = serializers.DateField()
    tipo_acto_administrativo = TipoActoAdministrativoSerializer()
    usuario = UserSerializer()
    tramite = serializers.IntegerField()
    alcaldia = serializers.IntegerField()
    urbanizacion = serializers.CharField()
