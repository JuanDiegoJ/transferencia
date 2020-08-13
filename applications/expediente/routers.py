from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register(r'expediente', viewsets.ExpedienteViewset, basename = 'expediente')

urlpatterns = router.urls