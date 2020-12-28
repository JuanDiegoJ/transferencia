from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register(r'caja', viewsets.CajasViewset, basename = 'caja')
router.register(r'carpeta', viewsets.CarpetaViewset, basename = 'carpetas')
router.register(r'documento', viewsets.DocumentosViewset, basename = 'documentos')

urlpatterns = router.urls