from django.shortcuts import render, get_object_or_404, redirect
from ..models import Libro, Pedido, UserProfile, Categoria
from django.contrib import messages
from unidecode import unidecode

def index(request):
  return render(request, 'administrador/index.html')

# USUARIO

# LIBRO
def admin_lista_libro(request):
  libros = Libro.objects.all()
  return render(request, 'administrador/libro/lista.html', {'libros': libros})

def admin_create_libro(request):
  if request.method == 'POST':
    nombre = request.POST['nombre']
    autor = request.POST['autor']
    editorial = request.POST['editorial']
    categoria = request.POST['categoria']
    descripcion = request.POST['descripcion']
    precio = request.POST['precio']
    stock = request.POST['stock']
    imagen = request.FILES['imagen']

    libro = Libro.objects.create(nombre=nombre, autor=autor, editorial=editorial, categoria=categoria, descripcion=descripcion, precio=precio, stock=stock, imagen=imagen)
    libro.save()

    return redirect('admin_lista_libro')
  else:
    return render(request, 'administrador/libro/create.html')

def admin_vista_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    return render(request, 'administrador/libro/vista.html', {'libro': libro})

# CATEGORIA

def admin_lista_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'administrador/categoria/index.html', {'categorias': categorias})

def admin_create_categoria(request):
  if request.method == 'POST':
    nombre = request.POST['nombre']
    url = unidecode(nombre.lower().replace(' ', '_'))

    categoria = Categoria.objects.create(nombre=nombre, url=url)
    categoria.save()

    messages.success(request, 'Creado correctamente')
    return redirect('admin_lista_categoria')
  else:
    return render(request, 'administrador/categoria/create.html')
