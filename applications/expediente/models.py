from django.db import models
from model_utils.models import TimeStampedModel
from applications.utilidades.models import (
    TipoActoAdministrativo,
    Tramite,
    Alcaldia,
    Modalidades
)
from applications.users.models import User
# Create your models here.

class Expediente(TimeStampedModel):

    no_radicacion = models.CharField('Expediente', max_length=20,unique=True)
    documento_final = models.CharField(
        'Documento final', 
        max_length=15
    )
    fecha_radicacion = models.DateField(
        'Fecha de radicación', 
        auto_now=False, 
        auto_now_add=False,
        blank=True,
        null=True
    )    
    fecha_expedicion = models.DateField(
        'Fecha de expedición', 
        auto_now=False, 
        auto_now_add=False,
        blank=True,
        null=True
    )    
    fecha_ejecutoria = models.DateField(
        'Fecha ejecutoria', 
        auto_now=False, 
        auto_now_add=False,
        blank=True,
        null=True
    )    
    fecha_inicio = models.DateField(
        'Fecha de inicio', 
        auto_now=False, 
        auto_now_add=False,
        blank=True,
        null=True
    )    
    fecha_final = models.DateField(
        'Fecha final', 
        auto_now=False, 
        auto_now_add=False,
        blank=True,
        null=True
    )    
    tipo_acto_administrativo = models.ForeignKey(
        TipoActoAdministrativo,
        on_delete = models.PROTECT,
    )
    usuario = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )

    def __str__(self):
        return f'{str(self.no_radicacion)}'

    class Meta:

        ordering = ['-no_radicacion']
        verbose_name = 'Expediente'
        verbose_name_plural = 'Expedientes'    


class InformacionGeneral(TimeStampedModel):

    no_radicacion = models.OneToOneField(
        Expediente,
        on_delete=models.CASCADE,
        primary_key=True
    )
    tramite = models.ForeignKey(
        Tramite,
        on_delete=models.CASCADE
    )
    alcaldia = models.ForeignKey(
        Alcaldia,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    urbanizacion = models.CharField(
        'Urbanización',
        max_length = 30,
        blank = True
    )
    modalidades = models.ManyToManyField(Modalidades, blank = True)

    def __str__(self):
        return self.no_radicacion.no_radicacion

    class Meta:

        ordering = ['-no_radicacion']
        verbose_name = 'Información General'
        verbose_name_plural = 'Información General'        


class ActuacionPosterior(TimeStampedModel):

    no_radicacion = models.ForeignKey(
        Expediente, 
        on_delete=models.CASCADE
    )
    cod_tipo_acto_administrativo = models.ForeignKey(
        TipoActoAdministrativo, 
        on_delete=models.CASCADE
    )
    acto_administrativo = models.CharField(
        'Acto administrativo', 
        max_length=20
    )
    fecha_expedicion = models.DateField(
        'Fecha de expedición', 
        auto_now=False, 
        auto_now_add=False,
        blank=True,
        null=True
    )    
    fecha_ejecutoria = models.DateField(
        'Fecha ejecutoria', 
        auto_now=False, 
        auto_now_add=False,
        blank=True,
        null=True
    )
    usuario = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )

    def __str__(self):
        return f'{self.no_radicacion} - {self.acto_administrativo}'

    class Meta:

        ordering = ['-no_radicacion']
        verbose_name = 'Actuación posterior'
        verbose_name_plural = 'Actuaciones posteriores' 
        constraints = [
            models.UniqueConstraint(fields=['no_radicacion', 'acto_administrativo'], name='unica_actuacion')
        ]


class Direcciones(TimeStampedModel):

    no_radicacion = models.ForeignKey(
        Expediente,
        on_delete=models.CASCADE
    )
    direccion = models.CharField(
        'Direccion',
        max_length = 50,
        blank = True
    )
    chip = models.CharField(
        'CHIP',
        max_length = 50,
        blank = True
    )
    matricula_inmobiliaria = models.CharField(
        'Matrícula inmobiliaría',
        max_length = 50,
        blank = True
    )
    anterior = models.BooleanField()
    usuario = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        blank = True,
        null = True
    )

    def __str__(self):
        return f'{self.direccion}'

    class Meta:

        ordering = ['-no_radicacion']
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'


class Fotos(TimeStampedModel):

    no_radicacion = models.ForeignKey(
        Expediente,
        on_delete=models.CASCADE
    )
    folios = models.CharField('Folios', max_length=30)

    def __str__(self):
        return self.folios

    class Meta:

        ordering = ['-no_radicacion']
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'