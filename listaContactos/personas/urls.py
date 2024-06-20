from django.urls import path
from personas.views import personasDeleteView, personasListView, personaTestView, personaCreateView, searchForHelp,  personasAnotherCreateView, personasShowObject

app_name = 'personas'
urlpatterns = [
    path('persona/', personaTestView, name='testViewPersona'),
    path('agregar/', personaCreateView, name='createPersona'),
    path('personas/<int:myID>/', personasShowObject, name = 'browsing'),
    path('', personasListView, name = 'listing'),
    path('personas/<int:myID>/delete', personasDeleteView, name = 'deleting'),
]