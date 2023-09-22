from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('registrar', views.registar, name='registrar'),
    path('logout', views.cerrar_sesion, name='logout'),
    path('administrador', views.admin, name='admin'),
    
    path('home', views.home, name='home'),
]
