from rest_framework import serializers

from apps.base.serializers import *
from apps.principal.models import *


class GeneroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genero
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

class SerieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Serie
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)
        read_only_fields = ['promedio_puntuaciones', 'promedio_puntuaciones_imdb']

    def to_representation(self,instance):
        generos = Genero.objects.filter(serie__id = instance.id).distinct()
        #list_generos = []
        list_generos_nombres = []
        for genero in generos:
            #list_generos.append(genero.id)
            list_generos_nombres.append(genero.nombre)
        
        return {
            'id': instance.id,
            'nombre': instance.nombre[0:40],
            #'genero': list_generos,
            'genero_nombre': list_generos_nombres,
            'sinopsis': instance.sinopsis[0:350],
            'fecha_salida': instance.fecha_salida.year,
            'promedio_puntuaciones': instance.promedio_puntuaciones,
            #'promedio_puntuaciones_imdb': instance.promedio_puntuaciones_imdb,
            #'link_imdb': instance.link_imdb,
            'cantidad_episodios': instance.cantidad_episodios,
            'color_carta': instance.color.nombre,
            #'image': instance['image'] if instance['image'] != '' else ''
            'image': instance.image.url if instance.image else '/media/none.png'
            }

class SerieSerializerDetail(SerieSerializer):
    def to_representation(self,instance):
        generos = Genero.objects.filter(serie__id = instance.id).distinct()
        #list_generos = []
        list_generos_nombres = []
        for genero in generos:
            #list_generos.append(genero.id)
            list_generos_nombres.append(genero.nombre)
        
        if instance.emision:
            emision = 'Leaving'
        else:
            emision = 'Finished'
        year = instance.fecha_salida.year
        month = int(instance.fecha_salida.month)
        temporada = "Winter"
        if month > 2 and month < 6:
            temporada = "Spring"
        if month > 5 and month < 9:
            temporada = "Summer"
        if month > 8 and month < 12:
            temporada = "Fall"
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            #'genero': list_generos,
            'genero_nombre': list_generos_nombres,
            'sinopsis': instance.sinopsis,
            'emision': emision,
            'fecha_salida': year,
            'temporada': temporada + " " + str(year) + " Season",
            'promedio_puntuaciones': instance.promedio_puntuaciones,
            #'promedio_puntuaciones_imdb': instance.promedio_puntuaciones_imdb,
            'link_imdb': instance.link_imdb if instance.link_imdb else "https://www.imdb.com/",
            'cantidad_episodios': instance.cantidad_episodios,
            'color_carta': instance.color.nombre,
            'image': instance.image.url if instance.image else '/media/none.png'
            }
class EpisodioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episodio
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

    def to_representation(self,instance):
        return {
            'id': instance.id,
            'serie': instance.serie.nombre,
            'nombre': instance.nombre,
            'link': instance.link
            }

class PuntuacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Puntuacion
        fields = ('id', 'serie', 'puntuacion')

