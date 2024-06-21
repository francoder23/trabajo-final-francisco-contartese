from django.db import models
from django.utils import timezone

class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "categoría de producto"
        verbose_name_plural = "categorías de producto"

class Producto(models.Model):
    categoria_id = models.ForeignKey(ProductoCategoria, null=True, blank=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=200)
    unidad_de_medida = models.CharField(max_length=200)
    cantidad = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(null=True, blank=True, editable=True, default=timezone.now)

    def __str__(self):
        return f"{self.nombre} ({self.unidad_de_medida} ${self.precio:.2f})"

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
