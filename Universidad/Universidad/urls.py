"""Universidad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from Universidad.Apps.Gestion.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, re_path
from django.contrib.auth import views as auth_views
from Universidad.Apps.Gestion.views import *


urlpatterns = [
    url('admin/', admin.site.urls),
    url('inicio/', inicio),
    url('registro/', registro),
    url('miPerfil/', miPerfil),

    url('ruedaObstetrica/', ruedaObstetrica, name='ruedaObstetrica'),

    url('editarPerfil/', editarPerfil,name='editarPerfil'),
    url('borrarUsuario/', borrarUsuario, name='borrarUsuario'),
    url('cambiarContra/', cambiar_contra, name='cambiarContra'),

    url('miDiario/', diario,name='diario'),

    url('inicioTension/', inicioTension, name='inicioTension'),
    url('anadirTension/', anadirTension,name='anadirTension'),
    url(r'^borrarTension/(?P<idTension>\d+)/$', borrarTension,name='borrarTension'),

    url('inicioPesoMama/', inicioPesoMama, name='inicioPesoMama'),
    url('anadirPesoMama/', anadirPesoMama,name='anadirPesoMama'),
    url(r'^borrarPeso/(?P<idPeso>\d+)/$', borrarPeso,name='borrarPeso'),

    url('inicioPesoBebe/', inicioPesoBebe, name='inicioPesoBebe'),
    url('anadirPesoBebe/', anadirPesoBebe,name='anadirPesoBebe'),

    url('inicioMedicacion/', inicioMedicacion, name='inicioMedicacion'),
    url('anadirMedicacion/', anadirMedicacion,name='anadirMedicacion'),
    url(r'^borrarMedicacion/(?P<idMedicacion>\d+)/$', borrarMedicacion,name='borrarMedicacion'),

    url('inicioMedida/', inicioMedida, name='inicioMedida'),
    url('anadirMedida/', anadirMedida,name='anadirMedida'),
    url(r'^borrarMedida/(?P<idMedida>\d+)/$', borrarMedida,name='borrarMedida'),

    url('inicioPatada/', inicioPatada, name='inicioPatada'),

    url('inicioContraccion/', inicioContraccion, name='inicioContraccion'),

    url('inicioSesion/', auth_views.LoginView.as_view(), name='inicioSesion'),
    url('cerrarSesion/', auth_views.LogoutView.as_view(), name='logout'),

    url('anadirFecha/', crearFechaCalendario, name='anadirFecha'),
    url(r'^borrarEvento/(?P<idEvento>\d+)/$', borrarEvento, name='borrarEvento'),
    url(r'^buscarFecha/$', buscarFecha, name='buscarFecha'),
    url(r'^miAgenda/$', agenda, name='agenda'),
    url(r'^miAgenda/?detalle=(?P<fechaDetalle>\d+)/$', agenda, name='agenda'),
    url(r'^miAgenda/?fecha=(?P<mes>[+|-]+\d+)&$', agenda, name='agenda'),
    url(r'^miAgenda/?fecha=(?P<mes>[+|-]+\d+)&detalle=(?P<fechaDetalle>\d+)/$', agenda, name='agenda'),

]