from django.contrib import admin

from apps.principal.models import *


# Register your models here.
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_display_links = list_display

class ColorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion",'image')
    list_display_links = list_display

class SerieAdmin(admin.ModelAdmin):
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

class EpisodioAdmin(admin.ModelAdmin):
    list_display = ("nombre","serie")
    list_display_links = list_display
    search_fields = list_display

class PuntuacionAdmin(admin.ModelAdmin):
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