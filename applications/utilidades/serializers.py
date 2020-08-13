from rest_framework import serializers

from .models import (
    Alcaldia, 
    Documento,
    Modalidades,
    TipoActoAdministrativo,
    Tramite
)

class AlcaldiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alcaldia
        fields = ('id', 'alcaldia')


class TipoActoAdministrativoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoActoAdministrativo
        fields = ('id')


class TramiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tramite
        fields = ('id', 'tramite')