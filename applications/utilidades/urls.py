from django.urls import path, include, re_path

from . import views

app_name = 'utilidades'

urlpatterns = [
    path(
        'api/alcaldias/',
        views.ListaAlcaldias.as_view(),
        name='alcaldias'
    ),
]