# MEGABIBLIOTECA

Solicita libros

## Requisitos de Instalación

Antes de comenzar con el desarrollo en este proyecto, asegúrate de tener los siguientes requisitos instalados en tu sistema:

- [Python](https://www.python.org/downloads/) (versión X.X o superior)
- [pip](https://pip.pypa.io/en/stable/installation/) (herramienta de gestión de paquetes de Python)

## Configuración del Entorno de Desarrollo

Sigue estos pasos para configurar el entorno de desarrollo:

1. Clona el repositorio desde GitHub:

```bash
git clone https://github.com/profe-benja/megabiblioteca-django
```

2. Instala las dependencias del proyecto desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

3. Realiza las migraciones iniciales de la base de datos:

```bash
python manage.py migrate
```

4. Crea un superusuario para acceder al panel de administración (sigue las instrucciones en la consola):

```bash
python manage.py createsuperuser
```

5. Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

6. Abre tu navegador y accede a [http://localhost:8000/](http://localhost:8000/) para ver la aplicación en funcionamiento.


7. puedes ir a la url de 
[http://localhost:8000/data](http://localhost:8000/data) para cargar informacion por defecto

- admin -> 12345
- cliente -> 12345
