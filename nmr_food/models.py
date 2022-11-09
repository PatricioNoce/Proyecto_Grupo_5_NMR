from django.db import models


class Configuracion(models.Model) :
    nombre_pagina = models.CharField(max_length=100)
    
    
class Menu(models.Model):
    comida = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=250, default='sin descripcion')
    image = models.ImageField(upload_to="menus", null=True, blank=True)
    
    
class Informacion(models.Model) :
    nombres_integrantes = models.CharField(max_length=100)
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=255)
    content = models.TextField(max_length=3000)
    date_published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="posts", null=True, blank=True)

    def __str__(self):
        return f"id:{self.id}, title:{self.title}"