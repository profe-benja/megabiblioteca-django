from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro, Pedido

# inicio de todo
def index(request):
    return render(request, 'index.html')

# AUTH
def login(request):
    if request.method == 'POST':
        # usuario = request.POST.get('usuario')
        # clave = request.POST.get('pass')
        # user = authenticate(request, username=usuario, password=clave)
        # if user is not None:
        #     profile = UserProfile.objects.get(user=user)
        #     request.session['perfil'] = profile.role
            
        #     login(request, user)
        return redirect('home')
        # else:
        #     context = {
        #         'error' : 'Error intente nuevamente.'
        #     }
        #     return render(request, 'auth/inicio_sesion.html', context)
    
    return render(request, 'auth/index.html')

def cerrar_sesion(request):
    return redirect('index')

# SISTEMA
def home(request):
    return render(request, 'home.html')

def admin(request):
    return render(request, 'admin/index.html')


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