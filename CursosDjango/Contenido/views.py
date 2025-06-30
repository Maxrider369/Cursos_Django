from django.shortcuts import render, HttpResponse

#Menu de direccionamiento.
def principal (request):
    return render(request, "inicio/principal.html")

def contacto (request):
    return render(request, "inicio/contacto.html")

def cursos (request):
    return render(request, "inicio/cursos.html")

def cursos_list(request):
    return HttpResponse("Listado de cursos")