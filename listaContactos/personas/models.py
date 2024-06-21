from django.db import models
from django.urls import reverse

# Create your models here.

class Persona(models.Model):
    nombre    = models.CharField(max_length = 100, blank=False)
    apellidos = models.CharField(max_length = 100, blank=False)
    edad      = models.IntegerField()
    email     = models.CharField(max_length = 100)
    donador   = models.BooleanField(default=False)
    dni       = models.CharField(max_length = 8, null=True)
    telefono  = models.CharField(max_length = 9, null=True)
    
    def get_absolute_url(self):
        return reverse('personas:persona-detail', kwargs = {'pk': self.id})