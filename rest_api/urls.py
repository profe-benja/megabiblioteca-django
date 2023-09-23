from django.urls import path
from . import views
# api/v1/
urlpatterns = [
    path('libro/', views.lista_libro, name='lista_libro'),
    path('libro/<id>', views.vista_libro, name='vista_libro'),
]
