
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name = 'home'),
    path('detalles_post/<slug:slug>/', detallesPost, name = 'detalles_post'),
    path('proyectos', proyectos, name = 'proyectos'),
    path('post', post, name = 'post'),
    path('videojuegos', videojuegos, name = 'videojuegos')
]