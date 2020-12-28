from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register(r'expediente', viewsets.ExpedienteViewset, basename = 'expediente')
router.register(r'actuaciones-posteriores', viewsets.ActuacionesPosterioresViewset, basename = 'actuaciones_posteriores')
router.register(r'direcciones', viewsets.DireccionesViewset , basename = 'direcciones')
router.register(r'fotos', viewsets.FotosViewset , basename = 'fotos')

urlpatterns = router.urls