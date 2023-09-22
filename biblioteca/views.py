from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro, Pedido, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from django.contrib.auth.models import User
from django.contrib import messages

# inicio de todo
def index(request):
    return render(request, 'index.html')

# AUTH
def inicio_sesion(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('pass')
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            profile = UserProfile.objects.get(user=user)
            request.session['perfil'] = profile.role
            
            login(request, user)   
            return redirect('home')
        else:
            context = {
                'error' : 'Error intente nuevamente.'
            }
            return render(request, 'auth/index.html', context)
    
    return render(request, 'auth/index.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def registar(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        first_name = request.POST.get('nombre')
        last_name = request.POST.get('apellido')
        email = request.POST.get('correo')
        password = request.POST.get('pass')
        
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

        role = request.POST.get('tipo')
        UserProfile.objects.create(user=user, role=role) 
        
        messages.success(request, 'Creado correctamente')
        
        return redirect('login')
    
    return render(request, 'auth/create.html')

def recuperar(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        nueva_contraseña = "123123"
        
        try:
            usuario = User.objects.get(email=correo)
            # Actualizar la contraseña utilizando set_password
            usuario.set_password(nueva_contraseña)
            usuario.save()
            messages.success(request, 'Contraseña actualizada correctamente.')
            return redirect('recuperar')
        except User.DoesNotExist:
            messages.error(request, 'No se encontró ningún usuario con ese correo electrónico.')
        
    return render(request, 'auth/recuperar.html')

# SISTEMA
def home(request):
    perfil = request.session.get('perfil') 
    context = {
        'perfil' : perfil,
    }
    
    return render(request, 'home.html', context)

def admin(request):
    return render(request, 'administrador/index.html')


# USUARIO

# LIBRO
def lista_libros(request):
    libros = Libro.objects.all()

    context = {
        'libros' : libros
    }
    
    return render(request, 'biblioteca/lista_libros.html', context)

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    
    context = {
        'libro' : libro
    }
    
    return render(request, 'biblioteca/detalle_libro.html', context)

def solicitar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    # Aquí puedes manejar la lógica de solicitud de libros
    return redirect('lista_libros')