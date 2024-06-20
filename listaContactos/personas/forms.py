from django import forms

from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'email',
            # no se encuentra el campo donador
            'dni',
            'telefono',
        ]
        
class RawPersonaForm(forms.Form):
    nombres   = forms.CharField()
    apellidos = forms.CharField()
    edad      = forms.IntegerField()
    donador   = forms.BooleanField()