from rest_framework import serializers
from biblioteca.models import Libro

class LibroSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')
    class Meta:
      model = Libro
      fields = '__all__'
      # fields = ['id', 'nombre', 'descripcion']
