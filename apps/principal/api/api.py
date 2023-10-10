from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.base.api import *
from apps.base.serializers import *
from apps.principal.api.serializers import *
from apps.principal.models import *
from apps.principal.views import *

class GeneroViewSet(GeneralViewSet):
    serializer_class = GeneroSerializer

class ColorViewSet(GeneralViewSet):
    serializer_class = ColorSerializer

class SerieViewSet(GeneralViewSet):
    serializer_class = SerieSerializer

    def retrieve(self, request, pk=None):
        model = self.get_serializer().Meta.model.objects.filter(state = True, id = pk).first()
        serializer = SerieSerializerDetail(model)
        return Response(serializer.data)

    def list(self, request):
        model = get_filter_serie(self, request)
        model = get_entrada(model, request)
        pagina, cant_pagina = chek_paginacion_str(request)
        if model:
            count = model.count()
            model = paginacion(model, pagina, cant_pagina)
            data = self.get_data(model)
            return Response({'count':count, 'results': data}, status = status.HTTP_200_OK)
        return Response({'message': 'Not found!'}, status = status.HTTP_400_BAD_REQUEST)
    

class EpisodioViewSet(GeneralViewSet):
    serializer_class = EpisodioSerializer

class PuntuacionViewSet(GeneralViewSet):
    serializer_class = PuntuacionSerializer
    permission_classes = [IsAuthenticated]

    def data_url(self, request):
        usuario = request.user.id
        if not usuario:
            return None
        serie = request.GET.get('serie')
        if not serie:
            return None
        if serie.isdigit():
            id_serie = int(serie)
            model = self.get_queryset().filter(serie_id = id_serie, usuario_id = usuario)
            #print({"serie": serie, "usuario": usuario, "model": model})
            return model
        return None

    def list(self, request):
        model = self.data_url(request)
        data = self.get_data(model)
        return Response(data, status = status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            usuario = request.user.id
            if not usuario:
                #usuario = serializer.data.get('usuario')
                return Response({'message': 'This user cannot change the score'}, status=status.HTTP_401_UNAUTHORIZED)
            serie = serializer.data.get('serie')
            puntuacion = serializer.data.get('puntuacion')
            print(usuario,serie, puntuacion)
            puntuacion_insert = Puntuacion(usuario_id = usuario, serie_id = serie, puntuacion = puntuacion)
            puntuacion_insert.save()
            model = self.data_url(request)
            data = self.get_data(model)
            return Response(data, status = status.HTTP_200_OK)
        return Response({'message': 'Invalid data!'}, status = status.HTTP_400_BAD_REQUEST)
