from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    tipo = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=30)
    precio= models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Facturas(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente