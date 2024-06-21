from django.urls import path
from estudiante.views import estudiante_list,index

app_name = "estudiante"

urlpatterns = [
    path("", index, name="index" ), 
    path("estudiante/list", estudiante_list, name= "estudiante_list")
 ]
