from rest_framework import serializers
from .models import *


class CajaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Caja
        fields = '__all__'


class CarpetaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Carpeta
        fields = '__all__'


class DocumentosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Document
        fields = '__all__'