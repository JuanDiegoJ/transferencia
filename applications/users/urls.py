from django.urls import path, re_path, include
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

app_name='users'

urlpatterns = [
    path(
        'api/registro/',
        views.RegistrarUsuarioAPI.as_view(),
        name='register'
    ),
    path(
        'api/login/',
        views.LoginAPI.as_view(),
        name='login'
    ),
    path(
        'api/renew/',
        TokenRefreshView.as_view(),
        name='renew'
    ),
]