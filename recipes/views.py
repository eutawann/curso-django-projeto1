from django.shortcuts import render
from django.http import HttpResponse

# HTTP REQUEST
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Tawan Carvalho'
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Tawan Carvalho'
    })

