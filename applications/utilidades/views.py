from rest_framework.generics import (
    ListAPIView,

)
from django.shortcuts import render
from .serializers import AlcaldiaSerializer
from .models import Alcaldia

class ListaAlcaldias(ListAPIView):

    serializer_class = AlcaldiaSerializer

    def get_queryset(self):
        return Alcaldia.objects.all()