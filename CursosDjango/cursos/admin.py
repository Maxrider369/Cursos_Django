from django.contrib import admin
from django.utils.html import format_html
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    # Cambiar títulos
    admin.site.site_header = "CURSOS"
    admin.site.site_title = "CONVOCATORIAS CURSOS"
    admin.site.index_title = "Panel de Administración - CONVOCATORIAS"

    # Mostrar imagen en la tabla con miniatura
    def imagen_miniatura(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="80" style="object-fit: cover;"/>', obj.imagen.url)
        return "Sin imagen"
    imagen_miniatura.short_description = 'Imagen'

    # Campos que se muestran en la lista
    list_display = ('imagen_miniatura', 'nombre', 'instructor', 'duracion_horas', 'precio', 'cupo_maximo', 'fecha_creacion')

    # Ordenar por fecha
    ordering = ('fecha_creacion',)

    # Barra de búsqueda
    search_fields = ('nombre', 'instructor', 'descripcion')

    # Filtros laterales
    list_filter = ('instructor', 'fecha_creacion', 'cupo_maximo')

    # Filtro por fecha
    date_hierarchy = 'fecha_creacion'

    # Campos del formulario
    fields = (
        ('nombre', 'instructor'),
        'descripcion',
        ('duracion_horas', 'precio', 'cupo_maximo'),
        'imagen',
        'fecha_creacion'
    )

    readonly_fields = ('fecha_creacion',)