from django.db import models
from django.utils import timezone
# Create your models here.


class Categoria(models.Model):
    """Modelo categoria"""
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """Modelo productos"""

    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    categoria = models.ForeignKey(
        Categoria, default=1, on_delete=models.CASCADE)

    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
