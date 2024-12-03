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
        
def agregar_comentario(request, post_id):
    if request.method == "POST":
        contenido = request.POST.get("contenido")
        
        post = Post.objects.get(id=post_id)
        
        #print(contenido)
        #print(post)
        #print(request.user)
        
        nuevo_comentario = Comentario(contenido=contenido, post=post, autor=request.user)
        
        nuevo_comentario.save()

        messages.success(request, "Comentario creado con éxito")
        return redirect('detalle_post', post_id)
    else:
        messages.error(request, "Acción / método no permitido")
        return redirect('posts')
    

@login_required(login_url="login")
@permission_required("blog.delete_comentario", login_url="home")
def eliminar_comentario(request, comentario_id):
    contexto = {}
    try:
        comentario = Comentario.objects.get(id=comentario_id)
        
        if comentario.autor != request.user:
            messages.error(request, f"Usted no es el autor del comentario, no puede eliminarlo")
            return redirect('posts')
        
    except comentario.DoesNotExist as e:
        messages.error(request, f"No existe un comentario con id: {comentario_id}")
        return redirect('posts')
    
    if request.method == "POST":
        comentario.delete()
        messages.success(request, "Comentario eliminado con éxito")
        return redirect('posts')
    else:
        # BLOQUE GET
        contexto["comentario"] = comentario 
        return render(request, 'blog/eliminar_comentario.html', contexto)
    
@login_required(login_url="login")
@permission_required("blog.add_post", login_url="home")
def crear_post(request):
    contexto = {}
    contexto["form"] = PostFormCreate()
        
    if request.method == 'GET':
        return render(request, 'blog/crear_post.html', contexto)
    
    if request.method == 'POST':
        
        form = PostFormCreate(request.POST)
        contexto["form"] = form 
        
        if form.is_valid():
            model_post = form.instance
            
            model_post.autor = request.user
            # print(model_post.autor.id)
            model_post.save()
            
            messages.success(request, "Post creado con éxito.")
            return redirect('posts')
            
        else:
            messages.error(request, "Algo ha fallado, revise bien los datos ingresados.")
            return render(request, 'blog/crear_post.html', contexto)