from django.db import models

class Cliente(models.Model) : 
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)


    def __str__(self):
        return f"Nombre:{self.nombre}, Telefono:{self.telefono}, Mail:{self.mail}, Direccion:{self.direccion}"

class Configuracion(models.Model) :
    nombre_pagina = models.CharField(max_length=100)