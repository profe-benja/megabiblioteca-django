from django.urls import path
from . import views
from .routes import viewsData

urlpatterns = [
  path('', views.index, name='index'),
  path('auth/login', views.inicio_sesion, name='login'),
  path('auth/registrar', views.registar, name='registrar'),
  path('auth/recuperar', views.recuperar, name='recuperar'),
  path('auth/logout', views.cerrar_sesion, name='logout'),

  #
  path('home', views.home, name='home'),
  path('home/categoria/<url>', views.home_categoria, name='home_categoria'),
  path('home/libro/<codigo>', views.home_libro, name='home_libro'),

  path('administrador', views.admin, name='admin'),
  path('administrador/libro', views.admin_lista_libro, name='admin_lista_libro'),
  path('administrador/libro/<id>', views.admin_vista_libro, name='admin_vista_libro'),
  # path('administrador/categoria', views.admin_vista_categoria, name='admin_vista_categoria'),

  # LIBRO
  path('libro', views.lista_libro, name='lista_libro'),
  # CATEGORIA
  path('categoria', views.lista_categoria, name='lista_categoria'),

  # path('libro/<nombre>', views.vista_libro, name='vista_libro'),

  path('data', viewsData.data, name='data'),
  path('vista_api', views.vista_api, name='data'),
]
