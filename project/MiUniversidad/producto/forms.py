from django import forms

from . import models

class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ProductoCategoria
        fields = ["nombre", "descripcion"]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = '__all__'
    template_name= "productoform.html"
     