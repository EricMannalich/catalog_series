from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.users.api.serializers import *

class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    list_serializer_class =  UserListSerializer
    queryset = None

    def get_object(self, pk):
        return self.serializer_class().Meta.model.objects.filter(id = pk).first()
        

    def get_queryset(self):
        if self.queryset is None:
            return self.serializer_class().Meta.model.objects.filter(is_active = True).values('id','username','email','first_name', 'image')
        return self.queryset

    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many = True)
        return Response(users_serializer.data,status = status.HTTP_200_OK)

    def create(self, request):
        user_serializer = self.serializer_class(data = request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            if user:
                json = user_serializer.data
                json['message'] = 'User successfully created!'
                return Response(json,status = status.HTTP_201_CREATED)
        return Response({'message':'User could not be created!', 'error':user_serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        user = self.get_object(pk)
        if user:
            user_serializer = self.serializer_class(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        return Response({'message':'A user with this data has not been found'},status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk = None):
        user = self.get_object(pk)
        if user:
            user_serializer = UserUpdateSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data,status = status.HTTP_200_OK)
            return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        return Response({'message':'A user with this data has not been found'},status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk = None):
        user = self.get_object(pk)
        if user:
            user_destroy = user.update(is_active = False)
            if user_destroy == 1:
                return Response({'message':'User successfully deleted!'},status = status.HTTP_200_OK)
            return Response({'message':'The user could not be deleted'},status = status.HTTP_400_BAD_REQUEST)
        return Response({'message':'A user with this data has not been found'},status = status.HTTP_400_BAD_REQUEST)
