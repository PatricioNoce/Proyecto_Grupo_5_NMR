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
    

class menu(models.Model):
    menuSeleccion = (
    ('Tacos', 'tacos'),
    ('Hamburguesa', 'hamburguesa'),
    ('Pizza', 'pizza'),
    ('Empanadas', 'empanadas'),
    )
    comida= models.CharField(max_length=20, choices=menuSeleccion, default='hamburguesa')
    precio= models.IntegerField()
    
class Informacion(models.Model) :
    nombres_integrantes = models.CharField(max_length=100)