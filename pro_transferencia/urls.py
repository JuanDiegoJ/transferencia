from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.utilidades.urls')),
    re_path('', include('applications.expediente.routers')),
    re_path('', include('applications.transferir.routers')),
]
