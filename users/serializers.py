
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tarjeta, UsuarioTarjeta, EstadoEspacio, Espacio, UsuarioEspacio, Tablero, Estado, EstadoTarjeta, Subtarea 

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user



class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'


class UsuarioTarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioTarjeta
        fields = '__all__'

class EstadoEspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoEspacio
        fields = '__all__'

class EspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacio
        fields = '__all__'

class UsuarioEspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioEspacio
        fields = '__all__'


class TableroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablero
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class EstadoTrajetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoTarjeta
        fields = '__all__'

class SubtareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtarea
        fields = '__all__'



