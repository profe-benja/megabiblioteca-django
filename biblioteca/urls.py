from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.cerrar_sesion, name='logout'),
    path('admin', views.admin, name='admin'),
    
    path('home', views.home, name='home'),
]
