from django.contrib import admin
from .models import ActuacionPosterior, Expediente, InformacionGeneral, Direcciones, Fotos
# Register your models here.

admin.site.register(ActuacionPosterior)
admin.site.register(Expediente)
admin.site.register(InformacionGeneral)
admin.site.register(Fotos)
admin.site.register(Direcciones)
