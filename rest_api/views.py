
from django.shortcuts import render
from .serializers import LibroSerializer
from biblioteca.models import Libro
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,)) #para que solo los usuarios autenticados puedan acceder a esta vista
def lista_libro(request):
    if request.method == 'GET':
        libros = Libro.objects.all() # select * from libro
        serializer = LibroSerializer(libros, many=True)
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
        
@csrf_exempt
@api_view(['GET','PUT','DELETE'])  
@permission_classes((IsAuthenticated,)) 
def vista_libro(request, id):
    try:
        libro = Libro.objects.get(id=id)
    except Libro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LibroSerializer(libro)
        return Response(serializer.data)

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