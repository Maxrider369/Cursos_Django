from django.shortcuts import render, get_object_or_404, redirect
from .forms import CursoForm
from .models import Curso

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos')  
    else:
        form = CursoForm()
    return render(request, 'cursos/crear_curso.html', {'form': form})

from .forms import CursoForm  # Debes tener un formulario para Curso

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/editar_curso.html', {'form': form})

def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos')
    return render(request, 'cursos/eliminar_curso.html', {'curso': curso})