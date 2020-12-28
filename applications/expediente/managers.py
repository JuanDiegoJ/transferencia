from django.db import models
from applications.utilidades.models import *

class ExpedienteManager(models.Manager):

    def informacion_expediente(self):
        expediente = self.values(
            'no_radicacion',
            'documento_final',
            'fecha_radicacion',
            'fecha_expedicion',
            'fecha_ejecutoria',
            'fecha_inicio',
            'fecha_final',
            'tipo_acto_administrativo'
        )
        return expediente

    def crear_o_actualizar_expediente(self, exp):
        obj, created = self.update_or_create(
            no_radicacion = exp['no_radicacion'],
            defaults = {
                'documento_final': exp['documento_final'],
                'fecha_radicacion': exp['fecha_radicacion'],
                'fecha_expedicion': exp['fecha_expedicion'],
                'fecha_ejecutoria': exp['fecha_ejecutoria'],
                'fecha_inicio': exp['fecha_inicio'],
                'fecha_final': exp['fecha_final'],
                'tipo_acto_administrativo': TipoActoAdministrativo.objects.filter(id=exp['tipo_acto_administrativo']).get()
            }
        )
        print(created)
        return obj


class InformacionGeneralManager(models.Manager):

    def crear_o_actualizar_informacion(self, expediente, informacion):

        obj, created = self.update_or_create(
            no_radicacion = expediente,
            defaults = {
                'tramite': Tramite.objects.filter(id=informacion['tramite']).get(),
                'alcaldia': Alcaldia.objects.filter(id=informacion['alcaldia']).get(),
                'urbanizacion': informacion['urbanizacion']
            }
        )

        for modalidad in obj.modalidades.all():
            obj.modalidades.remove(modalidad)

        modalidades = Modalidades.objects.filter(
            id__in = informacion['modalidades']
        )

        for modalidad in modalidades:
            obj.modalidades.add(modalidad)
        print(created)

        return obj

