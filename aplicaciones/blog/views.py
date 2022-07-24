
from .models import *
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-fecha_creacion')[:]

    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)


    return render(request, 'home.html',{'posts':posts})


def error404(request):
    return render(request, 'not_found.html')

# ------------------------Search Navbar-----------------------------------------

def search(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Project.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    print(posts)

    return render(request, '_navbar.html')

#------------------------Post y detalles----------------------------------------
def post(request):
    posts = Post.objects.all().order_by('-fecha_creacion')[:]
    # posts = Post.objects.all().order_by('-fecha_creacion')[:2]

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'post.html', {'posts': posts})

def detallesPost(request, slug):
    posts = Post.objects.filter(slug = slug)
    print(posts)
    return render(request, 'detalles_post.html', {'posts':posts})

# ------------------------- Pages----------------------------------------------------

def proyectos(request):
    projects = Project.objects.all()
    return render(request, 'proyectos.html', {'projects':projects})


#------------------- Vistas de las diferentes categorias-------------------------------

def tecnologia(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.filter(nombre__iexact = 'Tecnología')
    )
    return render(request, 'tecnologia.html', {'posts':posts})

def general(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact  = 'General')
    )
    return render(request, 'general.html', {'posts':posts})

def videojuegos(request):
    posts = Post.objects.filter(
        estado = False,
        categoria = Categoria.objects.get(nombre__iexact  = 'VideoJuegos')
    )
    return render(request, 'categorias/videojuegos.html', {'posts':posts})



# ---------------------------------Login----------------------------------------------

def login(request):
    return render(request, 'login.html')

# ---------------------------------Logout----------------------------------------------

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f" Usuario {username} creado")
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form' : form})