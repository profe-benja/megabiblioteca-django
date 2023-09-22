from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro, Pedido, EstadoPedido

# inicio de todo
def index(request):
    return render(request, 'index.html')

# AUTH
def inicio_sesion(request):
    return render(request, 'biblioteca/index.html')

def cerrar_sesion(request):
    return render(request, 'biblioteca/index.html')

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