from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myHomeView(request, *args, **kwargs):
    myContext = {
        'myText': 'Esto es sobre nosostros',
        'myNumber': 123,
    }
    return render(request, "home.html", myContext)
    
def anotherView(request):
    return HttpResponse('<h1>Solo otra página</h1>')