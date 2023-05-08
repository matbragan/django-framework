from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def milena(request):
    return HttpResponse('hi, my name is nena')

def matheus(request):
    return HttpResponse('chumbreksbreibol')
