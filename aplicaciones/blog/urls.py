
from django.urls import path
from .views import home, post, proyectos


urlpatterns = [
    path('', home, name = 'home'),
    path('proyectos', proyectos, name = 'proyectos'),
    path('post', post, name = 'post'),
]