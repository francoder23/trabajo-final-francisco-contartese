from django.shortcuts import render
from estudiante.models import Estudiante
def index(request):
    return render(request, "estudiante/index.html")


def estudiante_list(request):
    consulta = Estudiante.objects.all()
    contexto = {"estudiantes":consulta}
    return render(request, "estudiante/estudiante_list.html", contexto)