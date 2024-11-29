from django.shortcuts import render
from django.forms import ValidationError
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group

from .forms import RegistroUsuarioForm, LoginUsuarioForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Create your views here.

def index_view(request):
    return render(request, 'usuarios/usuarios.html', {})

def registro_view(request):
    form = None
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            
            # content_type = ContentType.objects.get_for_model(Producto)
            
            # # obtenemos el permiso a asignar
            # ver_productos_vip = Permission.objects.get(codename='productos_vip', content_type=content_type)
        
            user = form.save() 
        
            # user.user_permissions.add(ver_productos_vip)
            
            group = Group.objects.get(name='clientes')
            
            user.groups.add(group)

            
            login(request, user)
            
            messages.success(request, f"Usuario {user.username} registrado con éxito.")
            return HttpResponseRedirect("/")
        else:
            messages.error(request, "Error al intentar registrar al usuario, por favor verifique los datos.")
            return render(request, 'usuarios/registro.html', {"form": form})
                
    else:
        form = RegistroUsuarioForm()
        return render(request, 'usuarios/registro.html', {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = LoginUsuarioForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            try:
                user = User.objects.get(email=email)
                
                if user.check_password(password):
                    login(request, user)
                    messages.success(request, f"Usuario {user.username} iniciado con éxito")
                    return HttpResponseRedirect("/")
                else:
                    messages.error(request, "Contraseña incorrecta. Verifique sus credenciales.")
            except User.DoesNotExist:
                messages.error(request, "El usuario con ese correo no existe.")
            except Exception as e:
                messages.error(request, "Ocurrió un error. Inténtelo nuevamente.")
        
        else:
            messages.error(request, "Formulario inválido. Por favor, revise los campos.")
    
    else:
        form = LoginUsuarioForm()
    
    return render(request, 'usuarios/login.html', {"form": form})
    
    
    
def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/') 

