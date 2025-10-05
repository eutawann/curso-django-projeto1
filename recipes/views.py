from django.shortcuts import render
from django.http import HttpResponse

# HTTP REQUEST
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Tawan Carvalho'
    })
    # return HTTP response

def contato(request):
    return render(request, 'recipes/contato.html')

def sobre(request):
    return HttpResponse("SOBRE")