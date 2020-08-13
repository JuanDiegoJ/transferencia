from django.db import models
# Create your models here.


class Alcaldia(models.Model):

    cod_alcaldia = models.IntegerField(unique = True)
    alcaldia = models.CharField('Alcaldía', max_length = 20, unique = True)

    def __str__(self):
        return self.alcaldia

    class Meta:

        ordering = ['alcaldia']
        verbose_name = 'Alcaldía'
        verbose_name_plural = 'Alcaldías'


class Tramite(models.Model):

    cod_tramite = models.IntegerField(unique = True)
    tramite = models.CharField('Trámite', max_length=70, unique = True)

    def __str__(self):
        return self.tramite

    class Meta:

        ordering = ['tramite']
        verbose_name = 'Trámite'
        verbose_name_plural = 'Trámites'


class TipoActoAdministrativo(models.Model):

    cod_acto_administrativo = models.IntegerField(unique = True)
    tipo_acto_administrativo = models.CharField('Tipo de acto administrativo', unique = True, max_length=50)

    def __str__(self):
        return self.tipo_acto_administrativo

    class Meta:

        ordering = ['tipo_acto_administrativo']
        verbose_name = 'Tipo de acto administrativo'
        verbose_name_plural = 'Tipos de actos administrativos'


class Documento(models.Model):

    documento = models.CharField('Documento', max_length=60, unique = True)

    def __str__(self):
        return self.documento

    class Meta:

        ordering = ['documento']
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'


class Modalidades(models.Model):

    cod_modalidad = models.IntegerField('Código de modalidad')
    modalidad = models.CharField('Código de modalidad', max_length=30)

    def __str__(self):
        return self.modalidad

    class Meta:

        ordering = ['modalidad']
        verbose_name = 'Modalidad'
        verbose_name_plural = 'Modalidades'