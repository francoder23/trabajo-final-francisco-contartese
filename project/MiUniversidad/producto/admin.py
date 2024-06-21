from django.contrib import admin

# Register your models here.
from .models import ProductoCategoria, Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "categoria_id",
        "nombre",
        "unidad_de_medida",
        "cantidad",
        "precio",
       
    )
    list_display_links = ("nombre",)
    list_filter = ("categoria_id",)
 
   
   
admin.site.register(ProductoCategoria)
admin.site.register(Producto, ProductoAdmin)