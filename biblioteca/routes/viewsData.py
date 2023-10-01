from django.shortcuts import redirect
from ..models import Libro, Pedido, UserProfile, Categoria
from django.contrib.auth.models import User

# RANDOM DATA
from faker import Faker
from django.contrib.auth import get_user_model
from django.conf import settings
import random
from unidecode import unidecode

# private

# Reemplazar espacios con guiones bajos, convertir a minúsculas y quitar acentos


def convertir_a_formato_variable(cadena):
    return unidecode(cadena.lower().replace(' ', '_'))

# guardar datos


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
    user = get_user_model().objects.create_user(
        username="admin", email="admin@gmail.com", password="12345")
    UserProfile.objects.create(user=user, role='admin')

    user = get_user_model().objects.create_user(username="cliente",
                                                email="cliente@gmail.com", password="12345")
    UserProfile.objects.create(user=user, role='cliente')

    # Crea usuarios de ejemplo con roles
    for _ in range(10):
        username = fake.user_name()
        email = fake.email()
        # password = fake.password()
        password = '123456'
        role = random.choice(roles)

        user = get_user_model().objects.create_user(
            username=username, email=email, password=password)
        UserProfile.objects.create(user=user, role=role)

    # Crea libros de ejemplo relacionados con categorías
    categorias = Categoria.objects.all()

    # images = ['img/libro1.png', 'img/libro2.png', 'img/libro3.png', 'img/libro4.png', 'img/libro5.png', 'img/libro6.png', 'img/libro7.png', 'img/libro8.png', 'img/libro9.png', 'img/libro10.png'']
    array_categorias = ['Ficción', 'Fantasía y Ciencia Ficción', 'Aventura',
                        'Clásicos de la Literatura', 'Literatura Infantil y Juvenil']

    for i in range(5):
        nombre_categoria = array_categorias[i]
        url = convertir_a_formato_variable(nombre_categoria)
        Categoria.objects.create(id=(i+1),nombre=nombre_categoria, url=url)

    array_libros = [
      ['Cien años de soledad', 'Gabriel García Márquez', 1, 'Una obra maestra de la literatura latinoamericana que narra la historia de la familia Buendía a lo largo de varias generaciones en el pueblo ficticio de Macondo.'],
      ['Matar a un ruiseñor', 'Harper Lee', 1, 'Esta novela clásica aborda temas de racismo y justicia en el sur de Estados Unidos durante la década de 1930.'],
      ['El Señor de los Anillos', 'J.R.R. Tolkien', 2, 'Una epopeya de fantasía que sigue las aventuras de Frodo Bolsón y su misión para destruir un anillo maligno.'],
      ['1984', 'George Orwell', 1, 'Una novela distópica que describe un futuro totalitario donde el gobierno controla todos los aspectos de la vida de sus ciudadanos.'],
      ['Orgullo y prejuicio', 'Jane Austen', 4, 'Una comedia romántica que explora las relaciones sociales y los prejuicios en la Inglaterra del siglo XIX.'],
      ['Don Quijote de la Mancha', 'Miguel de Cervantes', 4, 'Esta obra es considerada la primera novela moderna y sigue las desventuras del caballero soñador Don Quijote.'],
      ['To Kill a Mockingbird', 'Harper Lee (en inglés)', 1, 'Una poderosa novela que aborda temas de racismo y justicia en el sur de Estados Unidos durante la década de 1930.'],
      ['El Principito', 'Antoine de Saint-Exupéry', 5, 'Un cuento filosófico que sigue las aventuras de un niño extraterrestre mientras viaja por diferentes planetas.'],
      ['Harry Potter (serie)', 'J.K. Rowling', 5, 'Una serie de libros que sigue las aventuras del joven mago Harry Potter mientras asiste a la escuela de magia Hogwarts.'],
      ['Crimen y castigo', 'Fiodor Dostoievski', 1, 'Esta novela psicológica sigue a Raskólnikov, un estudiante que comete un asesinato y enfrenta las consecuencias morales.'],
      ['Moby Dick', 'Herman Melville', 3, 'Una novela épica que sigue la obsesión del capitán Ahab por cazar al gran cachalote blanco Moby Dick.'],
      ['Los juegos del hambre', 'Suzanne Collins', 3, 'En un futuro distópico, Katniss Everdeen se convierte en voluntaria para los Juegos del Hambre para salvar a su hermana menor.'],
      ['El Alquimista', 'Paulo Coelho', 1, 'Sigue la historia de Santiago, un joven pastor que emprende un viaje en busca de su tesoro personal y su destino.'],
      ['El Gran Gatsby', 'F. Scott Fitzgerald', 4, 'Una novela que explora la decadencia y el sueño americano en la alta sociedad de la década de 1920.'],
      ['Las Crónicas de Narnia (serie)', 'C.S. Lewis', 5, 'Una serie de libros que transporta a los lectores a un mundo mágico poblado por criaturas fantásticas y aventuras emocionantes.'],
      ['El Código Da Vinci', 'Dan Brown', 1, 'Un thriller que sigue a Robert Langdon mientras descifra códigos y misterios para resolver un enigma que podría cambiar la historia.'],
      ['Anna Karenina', 'León Tolstói', 4, 'Explora las complejidades de las relaciones humanas y la moral en la alta sociedad rusa del siglo XIX.'],
      ['Pride and Prejudice', 'Jane Austen (en inglés)', 1, 'Una novela clásica que sigue las intrigas románticas de Elizabeth Bennet y Mr. Darcy en la Inglaterra del siglo XIX.'],
      ['Drácula', 'Bram Stoker', 1, 'Un clásico del terror que presenta al legendario vampiro Conde Drácula y su confrontación con un grupo de cazadores de vampiros.'],
      ['Canción de hielo y fuego (serie)', 'George R.R. Martin', 2, 'Una serie de libros épica que forma la base para la popular serie de televisión "Game of Thrones".']
    ]


    for _ in range(20):
        lib = array_libros[random.randint(0, 19)]
        # nombre_libro = fake.sentence()
        nombre_libro = lib[0]
        autor = lib[1]
        categoria_id = lib[2]
        codigo_libro = fake.unique.random_number()
        descripcion_libro = lib[3]
        # descripcion_libro = fake.paragraph()
        stock_libro = random.randint(1, 100)
        imagen = 'img/libro' + str(random.randint(1, 10)) + '.png'

        Libro.objects.create(
            nombre=nombre_libro,
            codigo=codigo_libro,
            descripcion=descripcion_libro,
            categoria_id=categoria_id,
            stock=stock_libro,
            imagen=imagen,
            autor=autor
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

    return redirect('index')
