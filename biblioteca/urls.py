from django.urls import path
from . import views
from .routes import viewsData
from .routes import viewsAdmin

urlpatterns = [
  path('', views.index, name='index'),
  path('auth/login', views.inicio_sesion, name='login'),
  path('auth/registrar', views.registar, name='registrar'),
  path('auth/recuperar', views.recuperar, name='recuperar'),
  path('auth/logout', views.cerrar_sesion, name='logout'),

  # pagina cliente
  path('home', views.home, name='home'),
  path('home/categoria/<url>', views.home_categoria, name='home_categoria'),
  path('home/libro/<codigo>', views.home_libro, name='home_libro'),

  # pagina administrador
  path('administrador', viewsAdmin.index, name='admin_index'),
  path('administrador/libro', viewsAdmin.admin_lista_libro, name='admin_lista_libro'),
  path('administrador/libro/create', viewsAdmin.admin_create_libro, name='admin_create_libro'),
  path('administrador/libro/<id>', viewsAdmin.admin_vista_libro, name='admin_vista_libro'),
  path('administrador/categoria', viewsAdmin.admin_lista_categoria, name='admin_lista_categoria'),
  path('administrador/categoria/create', viewsAdmin.admin_create_categoria, name='admin_create_categoria'),
  # path('administrador/categoria/<id>', viewsAdmin.admin_vista_categoria, name='admin_vista_categoria'),

  # LIBRO
  # path('libro', views.lista_libro, name='lista_libro'),
  # CATEGORIA
  # path('categoria', views.lista_categoria, name='lista_categoria'),

  # path('libro/<nombre>', views.vista_libro, name='vista_libro'),

  path('data', viewsData.data, name='data'),
  path('vista_api', views.vista_api, name='data'),
]
