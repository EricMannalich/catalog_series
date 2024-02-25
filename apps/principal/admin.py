from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from apps.principal.models import *

class GeneroResource(resources.ModelResource):
    class Meta:
        model = Genero

class GeneroAdmin(ImportExportModelAdmin):
    resource_class = GeneroResource
    list_display = ("nombre", "descripcion")
    list_display_links = list_display

class ColorResource(resources.ModelResource):
    class Meta:
        model = Color

class ColorAdmin(ImportExportModelAdmin):
    resource_class = ColorResource
    list_display = ("nombre", "descripcion",'image')
    list_display_links = list_display

class SerieResource(resources.ModelResource):
    class Meta:
        model = Serie

class SerieAdmin(ImportExportModelAdmin):
    resource_class = SerieResource
    fieldsets = (
        ('Identidad', {
            'fields' : ('nombre','sinopsis','fecha_salida','image','cantidad_episodios','link_imdb',),
        }),
        ('Grupos', {
            'fields' : ('categoria','genero',),
            'description' : 'Grupos en común',
        }),
        ('Control', {
            'fields' : ('state','emision', 'color',),
            'classes' : ('collapse',),
        }),
        ('Recomendación', {
            'fields' : ('promedio_puntuaciones','promedio_puntuaciones_imdb'),
            'description' : 'Datos calculados de la interacción con los usuarios',
            'classes' : ('collapse',),
        }),
    )
    list_display = ("nombre","emision", 'color', "fecha_salida", "promedio_puntuaciones", "promedio_puntuaciones_imdb","categoria", "cantidad_episodios")
    list_display_links = list_display
    search_fields = ("nombre", "sinopsis",)
    list_filter = ("emision", 'color', "genero",)
    date_hierarchy = ("fecha_salida")

class EpisodioResource(resources.ModelResource):
    class Meta:
        model = Episodio

class EpisodioAdmin(ImportExportModelAdmin):
    resource_class = EpisodioResource
    list_display = ("nombre","serie")
    list_display_links = list_display
    search_fields = list_display

class PuntuacionResource(resources.ModelResource):
    class Meta:
        model = Puntuacion

class PuntuacionAdmin(ImportExportModelAdmin):
    resource_class = PuntuacionResource
    list_display = ("usuario","serie", "puntuacion")
    list_display_links = list_display
    search_fields = ("usuario","serie")
    list_filter = ("puntuacion",)

admin.site.register(Genero, GeneroAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Categoria)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Episodio, EpisodioAdmin)
admin.site.register(Puntuacion, PuntuacionAdmin)
