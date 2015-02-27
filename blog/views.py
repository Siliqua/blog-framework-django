# Create your views here.

from blog.models import Blog, Categoria
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('index.html', {
        'categorias': Categoria.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    return render_to_response('view_categoria.html', {
        'categoria': categoria,
        'posts': Blog.objects.filter(categoria=categoria)[:5]
    })
