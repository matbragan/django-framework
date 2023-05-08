from django.urls import path

from recipes.views import home, milena, matheus

urlpatterns = [
    path('', home),
    path('milena/', milena),
    path('matheus/', matheus)
]