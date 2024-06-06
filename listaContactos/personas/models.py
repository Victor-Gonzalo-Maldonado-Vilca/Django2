from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre    = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    edad      = models.IntegerField()
    email     = models.CharField(max_length = 100)
    donador   = models.BooleanField(default=False)
<<<<<<< HEAD
    dni       = models.CharField(max_length = 8, default="--------")
=======
    dni       = models.CharField(max_length = 8, default="--------")
    telefono  = models.CharField(max_length = 9, default="---------")
>>>>>>> pruebas
