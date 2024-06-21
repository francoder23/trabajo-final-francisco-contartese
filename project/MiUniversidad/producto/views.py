from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from producto.models import ProductoCategoria, Producto
from producto.forms import ProductoCategoriaForm, ProductoForm

def index(request):
    return render(request, "producto/index.html")

class ProductoCategoriaList(ListView):
    model = ProductoCategoria

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda) | Q(descripcion__icontains=busqueda)
            )
        return queryset

class ProductoCategoriaCreate(LoginRequiredMixin, CreateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")

class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria

class ProductoCategoriaActualizar(UpdateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")

class ProductoCategoriaDelete(DeleteView):
    model = ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")

class ProductoList(ListView):
    model = Producto

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)
        return queryset

class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("producto:producto_list")

class ProductoDetail(DetailView):
    model = Producto

class ProductoActualizar(UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("producto:producto_list")

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy("producto:producto_list")


