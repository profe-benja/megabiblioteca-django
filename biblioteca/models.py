from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='libros/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class EstadoPedido(models.Model):
    nombre = models.CharField(max_length=20)

class Pedido(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cliente = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE)
