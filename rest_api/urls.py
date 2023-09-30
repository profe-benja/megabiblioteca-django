from django.urls import path
from . import views
from . import viewsLogin
# api/v1/
urlpatterns = [
    path('auth/', viewsLogin.login, name='api_auth'),
    
    path('libro/', views.lista_libro, name='lista_libro'),
    path('libro/<id>', views.vista_libro, name='vista_libro'),
]
