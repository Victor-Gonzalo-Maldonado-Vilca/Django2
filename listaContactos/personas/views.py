from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

# Create your views here.

def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    context = {
        'objeto': obj,
    }
    return render(request, 'personas/description.html', context)

def personaCreateView(request):
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PersonaForm()
        
    context = {
        'form': form
    }
    
    return render(request, 'personas/personasCreate.html', context)
    
def searchForHelp(request):
    print('GET: ', request.GET)
    print('POST: ', request.POST)
    return render(request, 'personas/search.html', {})