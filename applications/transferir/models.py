import datetime
from django.db import models
from model_utils.models import TimeStampedModel
from applications.expediente.models import Expediente
from applications.utilidades.models import Documento
# Create your models here.


class Caja(TimeStampedModel):

    YEAR_CHOICES = []
    for r in range(2015, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    numero_caja = models.PositiveIntegerField()
    año = models.PositiveIntegerField(
        'Año',
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
    )

    def __str__(self):
        return f'{self.numero_caja} - {self.año}'

    class Meta:

        ordering = ['-año']
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas' 


class Document(TimeStampedModel):

    class TipoDocumento(models.IntegerChoices):
        FOLIOS = 1
        ARQUITECTURA = 2
        ESTRUCTURAL = 3

    no_radicacion = models.ForeignKey(
        Expediente,
        on_delete=models.CASCADE,
    )
    document = models.ForeignKey(
        Documento,
        on_delete=models.CASCADE
    )
    tipo_documento = models.PositiveIntegerField(
        'Tipo de documento',
        choices=TipoDocumento.choices
    )
    cantidad = models.PositiveIntegerField(
        'Cantidad',
        default=0
    )

    def __str__(self):
        return self.documento

    class Meta:

        ordering = ['-document']
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    
class Carpeta(models.Model):

    class TipoCarpeta(models.IntegerChoices):
        FOLIOS = 1
        ARQUITECTURA = 2
        ANEXOS = 3

    no_radicacion = models.ForeignKey(
        Expediente,
        on_delete=models.CASCADE
    )
    tipo_carpeta = models.PositiveIntegerField(
        'Tipo de carpeta',
        choices=TipoCarpeta.choices
    )
    caja = models.ForeignKey(
        Caja,
        on_delete=models.CASCADE
    )
    cantidad_ini = models.PositiveIntegerField(
        'Cantidad inicial',
        default=0
    )
    cantidad_final = models.PositiveIntegerField(
        'Cantidad final',
        default=0
    )
    carpeta_inicial = models.PositiveIntegerField(
        'Carpeta inicial'
    )
    carpeta_final = models.PositiveIntegerField(
        'Carpeta final'
    )
    
    def __str__(self):
        return f'{self.no_radicacion} {self.TipoCarpeta}'

    class Meta:

        ordering = ['-no_radicacion']
        verbose_name = 'Carpeta'
        verbose_name_plural = 'Carpetas'