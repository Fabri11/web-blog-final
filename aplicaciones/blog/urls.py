
from django.urls import path
from django.contrib.auth.views import logout_then_login, LoginView
from .views import *


urlpatterns = [
    path('home', home, name = 'home'),
    path('detalles_post/<slug:slug>/', detallesPost, name = 'detalles_post'),
    path('proyectos', proyectos, name = 'proyectos'),
    path('project_form', projectForm, name = 'subir_proyecto'),
    path('post', post, name = 'post'),
    path('videojuegos', videojuegos, name = 'videojuegos'),
    path('general', general, name = 'general'),
    path('preguntas', preguntas, name = 'preguntas'),
    path('tecnologia', tecnologia, name = 'tecnologia'),
    path('about_me', about_me, name = 'about_me'),
    path('', LoginView.as_view(template_name = 'user/login.html'), name = 'login'),
    path('', logout_then_login, name = 'logout'),
    path('register', register, name = 'register')
]