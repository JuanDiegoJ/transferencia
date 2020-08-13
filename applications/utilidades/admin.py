from django.contrib import admin
from .models import Alcaldia, Documento, TipoActoAdministrativo, Tramite, Modalidades
# Register your models here.
admin.site.register(Alcaldia)
admin.site.register(Documento)
admin.site.register(TipoActoAdministrativo)
admin.site.register(Tramite)
admin.site.register(Modalidades)