from django.db import models

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