from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendedor")
    celular = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return self.usuario.username

class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True, blank=True)
    producto = models.ForeignKey("producto.Producto", on_delete=models.DO_NOTHING)
    cantidad = models.PositiveBigIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:
        ordering = ("-fecha_venta",)

    def clean(self):
        if self.cantidad > self.producto.cantidad:
            raise ValidationError("Cantidad de productos limitada")

    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)

