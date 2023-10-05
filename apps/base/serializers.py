from rest_framework import serializers
from apps.base.models import *


class NombreSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=30, default="")

class BuscarSerializer(serializers.Serializer):
    entrada = serializers.CharField(max_length=50, default="", required=False,allow_null=True)
    pagina = serializers.IntegerField(default=1, required=False,allow_null=True)
    cant_pagina = serializers.IntegerField(default=10, required=False,allow_null=True)
    
class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

class FiltroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filtro
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

class EndBarSerializer(serializers.ModelSerializer):

    class Meta:
        model = EndBar
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)