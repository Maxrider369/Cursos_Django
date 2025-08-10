from django.shortcuts import render, HttpResponse
from cursos.models import Curso

#Menu de direccionamiento.
def principal (request):
    return render(request, "inicio/principal.html")

def contacto (request):
    return render(request, "inicio/contacto.html")

def cursos (request):
    cursos = Curso.objects.all()
    return render(request, "inicio/cursos.html", {'cursos': cursos})

