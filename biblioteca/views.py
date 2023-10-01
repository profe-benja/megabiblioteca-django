from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro, Pedido, UserProfile, Categoria
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from django.contrib.auth.models import User
from django.contrib import messages

## REQUESTS
import requests
from django.http import JsonResponse

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
    categorias = Categoria.objects.all()

    context = {
        'perfil' : perfil,
        'libros' : libros,
        'categorias': categorias,
        'categoria': None
    }

    return render(request, 'home.html', context)

def home_categoria(request, url):
    perfil = request.session.get('perfil')
    categorias = Categoria.objects.all()

    categoria = Categoria.objects.get(url=url)
    libros = categoria.libro_set.all()

    context = {
        'perfil' : perfil,
        'libros' : libros,
        'categorias': categorias,
        'categoria': categoria
    }

    return render(request, 'home.html', context)

def home_libro(request, codigo):
    perfil = request.session.get('perfil')
    libro = Libro.objects.get(codigo=codigo)

    context = {
        'perfil' : perfil,
        'libro' : libro,
    }

    return render(request, 'libro.html', context)

def admin(request):
    return render(request, 'administrador/index.html')



# USUARIO

# LIBRO
def lista_libro(request):
    if request.method == 'GET':
        libros = Libro.objects.all() # select * from libro
        serializer = LibroSerializer(libros, many=True)

        for libro_data in serializer.data:
          libro_data['imagen'] = settings.BASE_URL + '/static' + libro_data['imagen']

        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LibroSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def vista_libro(request, id):
    libro = Libro.objects.get_object_or_404(id=id)

        # return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
      context = {
        'libro' : libro
      }
      return render(request, 'biblioteca/libro/show.html', context)

    elif request.method == 'PUT' or request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = LibroSerializer(libro, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




def lista_libros(request):
    libros = Libro.objects.all()



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

# GET - POST /libro/
def lista_libro(request):
    if request.method == 'GET':
        libros = Libro.objects.all() # select * from libro
        context = {
            'libros' : libros
        }

        return render(request, 'libro.index', context)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = LibroSerializer(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         print('error', serializer.errors)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def lista_categoria(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all() # select * from libro
        context = {
            'categorias' : categorias
        }

        return render(request, 'categoria.index', context)

def vista_api(request):
    api_url = "https://rickandmortyapi.com/api/character/1"

    try:
        # Realizar una solicitud GET a la API principal
        response = requests.get(api_url)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            rick_data = response.json()
            context = {
                'rick' : rick_data
            }
            return render(request, 'api/rick.html', context)

        # Si la solicitud a la API principal falló
        else:
            return JsonResponse({"error": "Error al obtener los datos de la API principal"}, status=response.status_code)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
