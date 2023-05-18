from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')


def vegetarian(request):
    return render(request, 'recipes/vegetarian.html')


def carnivore(request):
    return HttpResponse('chumbreksbreibol')
