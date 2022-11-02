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
from NMR_Food.views import (index, 
                            about, HomeView, BuscarMenu, ListMenu, CreateMenu, DeleteMenu, UpdateMenu, DetailMenu,
                             Nmr_Login, Nmr_Logout, RegistroPagina )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nmr_food/', index),
    path('home/', HomeView.as_view(), name='home'),
    path('menu-buscar/', BuscarMenu.as_view()),
    path('about/', about, name='acerca_de_mi'),
    path('panel-menu/', ListMenu.as_view(), name="menu-list"),
    path('panel-menu/crear', CreateMenu.as_view(), name='menu-create'),
    path('panel-menu/<int:pk>/borrar', DeleteMenu.as_view(), name='menu-delete'),
    path('panel-menu/<int:pk>/actualizar', UpdateMenu.as_view(), name='menu-update'),
    path('panel-menu/<int:pk>/detail', DetailMenu.as_view(), name="menu-detail"),
    path('login/', Nmr_Login.as_view(), name="login"),
    path('logout/', Nmr_Logout.as_view(), name="logout"),
    path('registro/', RegistroPagina.as_view(), name='registro'),
]
