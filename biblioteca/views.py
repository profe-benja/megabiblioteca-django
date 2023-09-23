from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro, Pedido, UserProfile, Categoria
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from django.contrib.auth.models import User
from django.contrib import messages


# RANDOM DATA
from faker import Faker
from django.contrib.auth import get_user_model
from django.conf import settings
import random

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

@login_required
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
@login_required
def home(request):
    perfil = request.session.get('perfil') 
    libros = Libro.objects.all()
    
    context = {
        'perfil' : perfil,
        'libros' : libros
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



def data(request):
    fake = Faker()
    roles = [role[0] for role in settings.ROLES]

    # Limpiar datos existentes si es necesario
    User.objects.all().delete()
    UserProfile.objects.all().delete()
    Categoria.objects.all().delete()
    Libro.objects.all().delete()
    Pedido.objects.all().delete()
    
    # crea 2 usuarios
    user = get_user_model().objects.create_user(username="admin", email="admin@gmail.com", password="12345")
    UserProfile.objects.create(user=user, role='admin')
    
    user = get_user_model().objects.create_user(username="cliente", email="cliente@gmail.com", password="12345")
    UserProfile.objects.create(user=user, role='cliente')
    
    # Crea usuarios de ejemplo con roles
    for _ in range(10):
        username = fake.user_name()
        email = fake.email()
        # password = fake.password()
        password = '123456'
        role = random.choice(roles)

        user = get_user_model().objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user, role=role)

    # Crea categorías de ejemplo
    for _ in range(5):
        nombre_categoria = fake.word()
        Categoria.objects.create(nombre=nombre_categoria)

    # Crea libros de ejemplo relacionados con categorías
    categorias = Categoria.objects.all()
    nombres_de_imagen = ['img/libro1.png', 'img/libro2.png']

    for _ in range(20):
        nombre_libro = fake.sentence()
        codigo_libro = fake.unique.random_number()
        descripcion_libro = fake.paragraph()
        categoria_libro = random.choice(categorias)
        stock_libro = random.randint(1, 100)
        imagen = random.choice(nombres_de_imagen)

        Libro.objects.create(
            nombre=nombre_libro,
            codigo=codigo_libro,
            descripcion=descripcion_libro,
            categoria=categoria_libro,
            stock=stock_libro,
            imagen=imagen,
        )

    # Crea pedidos de ejemplo relacionados con libros y usuarios
    libros = Libro.objects.all()
    usuarios = get_user_model().objects.all()
    for _ in range(30):
        libro_pedido = random.choice(libros)
        cliente_pedido = random.choice(usuarios)
        estado_pedido = random.randint(1, 3)

        Pedido.objects.create(
            libro=libro_pedido,
            cliente=cliente_pedido,
            estado=estado_pedido,
        )

    messages.success(request, 'Datos creados correctamente')
    return redirect('index')