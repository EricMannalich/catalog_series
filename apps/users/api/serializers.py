from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.models import User


"""class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass"""
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'image' )
    def to_representation(self,instance):
        url_imagen = "/media/user.png"
        imagen = instance.image
        if imagen:
            url_imagen = imagen.url
        return {
            'id': instance.id,
            'username': instance.username,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'image': url_imagen
        }
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups','user_permissions', 'password')
    
    def create(self,validated_data):
        user = self.Meta.model(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self,instance,validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self,instance):
        url_imagen = "/media/user.png"
        imagen = instance['image']
        if imagen:
            url_imagen = imagen
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'image': url_imagen
        }


