from django.urls import path
from producto.views import index
from producto.views import (
ProductoCategoriaList, 
ProductoCategoriaCreate,
ProductoCategoriaDetail, 
ProductoCategoriaActualizar, 
ProductoCategoriaDelete,
ProductoList,
ProductoCreate,
ProductoDelete,
ProductoDetail,
ProductoActualizar,
)



app_name = "producto"

urlpatterns = [
    path("", index, name="index" ),
    #path("productocategoria/create", productocategoria_create, name="productocategoria_create"),
    #path("productocategoria/delete/<int:pk>", productocategoria_delete, name="productocategoria_delete"),
    #path("productocategoria/detail/<int:pk>", productocategoria_detail, name="productocategoria_detail"),
    #path("productocategoria/list", productocategoria_list, name= "productocategoria_list"),
    #path("productocategoria/actualizar/<int:pk>", productocategoria_actualizar, name="productocategoria_actualizar"),
 ]

urlpatterns += [
    path("productocategoria/list", ProductoCategoriaList.as_view(), name= "productocategoria_list"),
    path("productocategoria/create", ProductoCategoriaCreate.as_view(), name="productocategoria_create"),
    path("productocategoria/detail/<int:pk>", ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
    path("productocategoria/actualizar/<int:pk>", ProductoCategoriaActualizar.as_view(), name="productocategoria_actualizar"),
    path("productocategoria/delete/<int:pk>", ProductoCategoriaDelete.as_view, name="productocategoria_delete")
]

urlpatterns += [
    path("producto/list", ProductoList.as_view(), name= "producto_list"),
    path("producto/create", ProductoCreate.as_view(), name="producto_create"),
    path("producto/detail/<int:pk>", ProductoDetail.as_view(), name="producto_detail"),
    path("producto/actualizar/<int:pk>", ProductoActualizar.as_view(), name="producto_actualizar"),
    path("producto/delete/<int:pk>", ProductoDelete.as_view, name="producto_delete")
]