import datetime

from django.contrib.postgres.search import SearchQuery, SearchVector
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import APIView

from apps.base.serializers import *

CANT_MIN_PAGINA = 5
MIN_YEAR = 1990
MAX_YEAR = datetime.datetime.now().year

def paginacion(model, pagina = 1, cant_pagina = CANT_MIN_PAGINA):
    model = model.all()[pagina * cant_pagina - cant_pagina:pagina * cant_pagina]
    return model

def chek_paginacion_int(pagina, cant_pagina):
    if pagina:
        if pagina < 1:
            pagina = 1
    else:
        pagina = 1
    if cant_pagina:
        if cant_pagina < CANT_MIN_PAGINA:
            cant_pagina = CANT_MIN_PAGINA
    else:
        cant_pagina = CANT_MIN_PAGINA
    return pagina, cant_pagina

def chek_paginacion_str(request):
    request_pagina = request.GET.get('pagina')
    request_cant_pagina = request.GET.get('cant_pagina')
    pagina = 1
    cant_pagina = CANT_MIN_PAGINA
    if request_pagina:
        if request_pagina.isdigit():
            pagina = int(request_pagina)
    if request_cant_pagina:
        if request_cant_pagina.isdigit():
            cant_pagina = int(request_cant_pagina)
    pagina, cant_pagina = chek_paginacion_int(pagina,cant_pagina)
    return pagina, cant_pagina

def get_entrada(model, request):
    entrada = request.GET.get('entrada')
    if entrada:
        if entrada != "":
            if len(entrada) == 1:
                model = model.filter(nombre__startswith = entrada[0].upper())
            else:
                #model = model.filter(nombre__icontains = entrada).distinct() | model.filter(sinopsis__icontains = entrada).distinct()
                model = model.annotate(search=SearchVector('nombre', 'sinopsis')).filter(search=SearchQuery(entrada, search_type='websearch'))
    return model  

def get_fecha(model, request):
    str_fecha_inicio = request.GET.get('fecha_inicio')
    if str_fecha_inicio:
        fecha_inicio = datetime.datetime.strptime(str_fecha_inicio,'%Y-%m-%d')
        if fecha_inicio.year > MIN_YEAR:
            model = model.filter(fecha_salida__gte = fecha_inicio)

    str_fecha_fin = request.GET.get('fecha_fin')
    if str_fecha_fin:
        fecha_fin = datetime.datetime.strptime(str_fecha_fin,'%Y-%m-%d')
        if fecha_fin.year <= MAX_YEAR:
            model = model.filter(fecha_salida__lte = fecha_fin)

    return model

def get_filter_serie(self, request):
    model = self.get_queryset()
    filtros = request.GET.get('filtros')
    if not filtros:
        filtros = "true"
    if filtros == "true":
        model = get_fecha(model, request)

        genero = request.GET.get('genero')
        if genero:
            list_genero = genero.split(",")
            for genero in list_genero:
                model = model.filter(genero = genero)

        tansmicion = request.GET.get('tansmicion')
        if tansmicion:
            if tansmicion == "saliendo":
                model = model.filter(emision = True)
            elif tansmicion == "terminado":
                model = model.filter(emision = False)

        puntuacion = request.GET.get('puntuacion')
        if puntuacion:
            if puntuacion.isdigit():
                int_puntuacion = int(puntuacion)
                if int_puntuacion > 0:
                    new_model = model.filter(promedio_puntuaciones__gte = int_puntuacion - 1)
                    if new_model:
                        model = new_model

        colores = request.GET.get('color_carta')
        if colores:
            list_color = colores.split(",")
            if list_color:
                model = model.filter(color__in = list_color).distinct()
                
        orden = request.GET.get('orden')
        if orden:
            if (orden == "nombre_ascendente"):
                model = model.order_by('nombre')
            elif (orden == "nombre_descendente"):
                model = model.order_by('-nombre')
            elif (orden == "fecha_ascendente"):
                model = model.order_by('fecha_salida')
            elif (orden == "fecha_descendente"):
                model = model.order_by('-fecha_salida')
            elif (orden == "episodios_ascendente"):
                model = model.order_by('cantidad_episodios')
            elif (orden == "episodios_descendente"):
                model = model.order_by('-cantidad_episodios')
            elif (orden == "puntuacion_ascendente"):
                model = model.order_by('promedio_puntuaciones')
            elif (orden == "puntuacion_descendente"):
                model = model.order_by('-promedio_puntuaciones')
    return model

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class GeneralViewSet(viewsets.ModelViewSet):
    serializer_class = None
    permission_classes = [ReadOnly]

    def get_data(self, model):
        return self.serializer_class(model, many = True).data

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def destroy(self,request,pk=None):
        if (request.user.is_staff):
            model = self.serializer_class().Meta.model.objects.filter(id = pk).first()
            if model:
                model.state = False
                model.save()
                return Response({'message': 'Correctly eliminated!'}, status = status.HTTP_200_OK)
        return Response({'message': 'Not found!'}, status = status.HTTP_400_BAD_REQUEST)

class MenuViewSet(GeneralViewSet):
    serializer_class = MenuSerializer

class FiltroViewSet(GeneralViewSet):
    serializer_class = FiltroSerializer

class EndBarViewSet(GeneralViewSet):
    serializer_class = EndBarSerializer

class IpAddressViewSet(GeneralViewSet):
    serializer_class = IpAddressSerializer

class IpAddressGraphicAPIView(APIView):
    serializer_model = IpAddressSerializer
    permission_classes = [ReadOnly]
    
    def get(self, request, format=None):
        model = self.serializer_model().Meta.model.objects.filter(state = True).order_by("country_name")
        old_labels = model.distinct("country_name").values_list("country_name")
        labels = []
        new_list_datasets = []
        for old_label in old_labels:
            labels.append(old_label[0])
            new_list_datasets.append(model.filter(country_name = old_label[0]).count())
        datasets = {"data": new_list_datasets}
        data = {'labels' : labels, 'datasets' : datasets}
        if data:
            return Response(data, status = status.HTTP_200_OK)
        return Response({'message': 'Not found!'}, status = status.HTTP_400_BAD_REQUEST)
    

class IpAddressMapAPIView(APIView):
    serializer_model = IpAddressSerializer
    permission_classes = [ReadOnly]
    
    def get(self, request, format=None):
        model = self.serializer_model().Meta.model.objects.filter(state = True).order_by("country_code2")
        old_labels = model.distinct("country_code2").values_list("country_code2")
        data = []
        for old_label in old_labels:
            data.append({'country' : old_label[0].lower(), 'value' : model.filter(country_code2 = old_label[0]).count()})
        if data:
            return Response(data, status = status.HTTP_200_OK)
        return Response({'message': 'Not found!'}, status = status.HTTP_400_BAD_REQUEST)