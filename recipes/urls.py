from django.urls import path

from recipes.views import home, matheus, milena

urlpatterns = [
    path('', home),
    path('milena/', milena),
    path('matheus/', matheus)
]