from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Tarjeta, UsuarioTarjeta, EstadoEspacio, Espacio, UsuarioEspacio, Tablero, Estado, EstadoTarjeta, Subtarea 
from .serializers import RegisterSerializer, TarjetaSerializer, UsuarioTarjetaSerializer, EstadoEspacioSerializer, EspacioSerializer, UsuarioEspacioSerializer, TableroSerializer, EstadoSerializer, EstadoTarjetaSerializer, SubtareaSerializer, UserSerializer


# Create your views here.

# Vista de registro de usuarios
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# Vista para mostrar el login
def loginView(request):
    return render(request, 'users/index.html') 


# Vista para la página de registro
def registroView(request):
    return render(request, 'users/registro.html')


# Vista para la página de workspace
def workspaceView(request):
    return render(request, 'users/workspace.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer

class UsuarioTarjetaViewSet(viewsets.ModelViewSet):
    queryset = UsuarioTarjeta.objects.all()
    serializer_class = UsuarioTarjetaSerializer

class EstadoEspacioViewSet(viewsets.ModelViewSet):
    queryset = EstadoEspacio.objects.all()
    serializer_class = EstadoEspacioSerializer

class EspacioViewSet(viewsets.ModelViewSet):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer

class UsuarioEspacioViewSet(viewsets.ModelViewSet):
    queryset = UsuarioEspacio.objects.all()
    serializer_class = UsuarioEspacioSerializer

class TableroViewSet(viewsets.ModelViewSet):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class EstadoTarjetaViewSet(viewsets.ModelViewSet):
    queryset = EstadoTarjeta.objects.all()
    serializer_class = EstadoTarjetaSerializer

class SubtareaViewSet(viewsets.ModelViewSet):
    queryset = Subtarea.objects.all()
    serializer_class = SubtareaSerializer







