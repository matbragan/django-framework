from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')


def milena(request):
    return HttpResponse('hi, my name is nena')


def matheus(request):
    return HttpResponse('chumbreksbreibol')
