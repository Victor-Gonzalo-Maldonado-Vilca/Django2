from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre    = models.charField(max_length = 100)
    apellidos = models.charField(max_length = 100)
    edad      = models.IntegerField(max_digits = 3)