from django.contrib import admin
from django.utils.html import format_html
from .models import Curso, Actividad  # Importa ambos modelos

# Personalización global del panel de administración
admin.site.site_header = "Convocatorias cursos"
admin.site.site_title = "CONVOCATORIAS CURSOS"
admin.site.index_title = "Panel de Administración - CONVOCATORIAS"

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    def imagen_miniatura(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="80" style="object-fit: cover;"/>', obj.imagen.url)
        return "Sin imagen"
    imagen_miniatura.short_description = 'Imagen'
    
    list_display = ('imagen_miniatura', 'nombre', 'instructor', 'duracion_horas', 'precio', 'cupo_maximo', 'fecha_creacion')
    ordering = ('fecha_creacion',)
    search_fields = ('nombre', 'instructor', 'descripcion')
    list_filter = ('instructor', 'fecha_creacion', 'cupo_maximo')
    date_hierarchy = 'fecha_creacion'

    fields = (
        ('nombre', 'instructor'),
        'descripcion',
        ('duracion_horas', 'precio', 'cupo_maximo'),
        'imagen',
        'fecha_creacion'
    )

    readonly_fields = ('fecha_creacion',)

    class Media:
        css = {
            "all": ("admin/css/admin.css",)
        }


# Nuevo modelo: Actividad
@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('id', 'curso', 'fecha_creacion')
    search_fields = ('curso__nombre', 'fecha_creacion')
    date_hierarchy = 'fecha_creacion'
    readonly_fields = ('id', 'fecha_creacion')
    class Media:
        css = {
            "all": ("admin/css/admin.css",)
        }
