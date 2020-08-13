from rest_framework import serializers
from .models import Expediente, InformacionGeneral
from applications.utilidades.models import TipoActoAdministrativo
from applications.utilidades.serializers import TipoActoAdministrativoSerializer, TramiteSerializer
from applications.users.serializers import UserSerializer


class InformacionGeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = InformacionGeneral
        fields = ('__all__')


class ExpedienteSerializerViewset(serializers.Serializer):

    pk = serializers.IntegerField()
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
        informacion_expediente = InformacionGeneralSerializer(query, many=True).data
        return informacion_expediente


class ArrayIntegerSerializer(serializers.ListField):

    child = serializers.IntegerField()


class ExpedienteCreacion(serializers.Serializer):

    no_radicacion = serializers.CharField()
    documento_final = serializers.CharField()
    fecha_radicacion = serializers.DateField()
    fecha_expedicion = serializers.DateField()
    fecha_ejecutoria = serializers.DateField()
    fecha_inicio = serializers.DateField()
    fecha_final = serializers.DateField()
    tipo_acto_administrativo = serializers.IntegerField()
    tramite = serializers.IntegerField()
    alcaldia = serializers.IntegerField()
    urbanizacion = serializers.CharField()
    modalidades = ArrayIntegerSerializer()