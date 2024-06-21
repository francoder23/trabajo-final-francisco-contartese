from django.http import HttpResponse


from django.shortcuts import render
from datetime import datetime


def saludar(request):
    return HttpResponse("Bienvenido a la universidad")
 
def segunda_vista(request):
    return HttpResponse("<h1> Universidad de finanzas </h1>")

def nombre(request, nombre:str, apellido:str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre},")
    



