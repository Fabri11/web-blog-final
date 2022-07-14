from django.shortcuts import render
from .models import Project, Post

# Create your views here.

def home(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    projects = Project.objects.all()
    if queryset:
        projects = Project.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    return render(request, 'home.html',{'projects':projects})


def proyectos(request):
    project = Project.objects.all()
    return render(request, 'proyectos.html', {'project':project})

def post(request):
    post = Post.objects.all()
    return render(request, 'post.html', {'post': post})



