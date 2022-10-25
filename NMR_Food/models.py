from django.db import models

# Create your models here.
class Cliente(models.Model) : 
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    direccion = models.CharField()