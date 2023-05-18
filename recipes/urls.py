from django.urls import path

from recipes.views import carnivore, home, vegetarian

urlpatterns = [
    path('', home),
    path('vegetarian/', vegetarian),
    path('carnivore/', carnivore)
]