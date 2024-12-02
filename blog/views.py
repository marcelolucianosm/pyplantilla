from django.shortcuts import render
from .models import Post, Categoria, Comentario
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import redirect

from .forms import PostFormCreate

def posts(request):
    contexto = {}
    posts = Post.objects.all().order_by("id")
    contexto['posts'] = posts
    return render(request,'blog/posts.html' ,contexto)

def detalle_post(request,post_id):
    contexto = {}
    
    try:
        post = Post.objects.get(id=post_id)
        
        comentarios = Comentario.objects.all().filter(post=post)
        
    except post.DoesNotExist as e:
        messages.error(request, f"No existe el Post : {post_id}")
        return redirect('posts')
    
    contexto["post"] = post
    contexto["comentarios"] = comentarios
    return render(request,'blog/detalle_post.html',contexto)
        