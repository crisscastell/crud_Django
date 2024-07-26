"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from peliculas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.pag_principal, name='inicio'),
    path('Peliculas', views.pag_peliculas, name='menu_peliculas'),
    path('Peliculas/guardar', views.guardar, name='guardar'),
    path('peliculas/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('peliculas/detalle/<int:id>', views.detalle, name='detalle'),
     path('Peliculas/editar', views.editar, name='editar'),
]
