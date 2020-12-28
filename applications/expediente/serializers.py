from rest_framework import serializers
from .models import *


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


class ActuacionPosteriorSerializer(serializers.ModelSerializer):


    class Meta:

        model = ActuacionPosterior
        fields = '__all__'


class DireccionesSerializer(serializers.ModelSerializer):


    class Meta:

        model = Direcciones
        fields = '__all__'


class FotosSerializer(serializers.ModelSerializer):


    class Meta:

        model = Fotos
        fields = '__all__'