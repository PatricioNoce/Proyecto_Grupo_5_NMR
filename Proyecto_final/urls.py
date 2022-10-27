"""Proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from operator import index
from django.contrib import admin
from django.urls import path
from NMR_Food.views import AltaCliente, BuscarCliente, mostrar_clientes, index, mostrar_menu, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nmr_food/', index),
    path('cliente-alta/', AltaCliente.as_view() ),
    path('cliente-buscar/', BuscarCliente.as_view()),
    path('mis-clientes/', mostrar_clientes),
    path('menu/', mostrar_menu),
    path('about/', about)
]
