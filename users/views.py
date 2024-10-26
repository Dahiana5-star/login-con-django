from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Tarjeta, UsuarioTarjeta, EstadoEspacio, Espacio, UsuarioEspacio, Tablero, Estado, EstadoTarjeta, Subtarea 
from .serializers import RegisterSerializer, TarjetaSerializer, UsuarioTarjetaSerializer, EstadoEspacioSerializer, EspacioSerializer, UsuarioEspacioSerializer, TableroSerializer, EstadoSerializer, EstadoTarjetaSerializer, SubtareaSerializer, UserSerializer
from django.http import JsonResponse

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Vista de registro de usuarios
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# Vista para mostrar el login
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Esto crea la sesión
        
            # Genera o recupera el token de autenticación
            token, created = Token.objects.get_or_create(user=user)
            
            # Devuelve tanto el token como el session_id
            return JsonResponse({'message': 'Login exitoso', 'token': token.key, 'session_id': request.session.session_key})

        else:
            return JsonResponse({'error': 'Credenciales incorrectas'}, status=400)
    return render(request, 'users/index.html')


# Vista para la página de registro
def registroView(request):
    return render(request, 'users/registro.html')


# Vista para la página de workspace
def workspaceView(request):
    return render(request, 'users/workspace.html')


@api_view(['GET'])
def getUser(request):
    username = request.GET.get('username')  # Obtener el parámetro 'username' de la URL
    if username:
        try:
            user = User.objects.get(username=username)
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                # Añade aquí cualquier otro campo que quieras devolver
            }
            return JsonResponse(user_data, safe=False)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    return JsonResponse({'error': 'Parámetro username no proporcionado'}, status=400)



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
    serializer_class = UsuarioEspacioSerializer
    
    def get_queryset(self):
        # Obtiene el valor del parámetro de consulta 'espacio' en la URL, si está presente
        espacio = self.request.query_params.get('espacio', None)
        
        # Filtra los resultados solo por el valor de espacio, si fue proporcionado
        if espacio is not None:
            queryset = UsuarioEspacio.objects.filter(espacio=espacio)
        
            if not queryset.exists():
                # Retorna un mensaje de error si el espacio no existe
                self.action = 'retrieve'  # Evita error por falta de método retrieve
                raise ValueError(f"No se encontró el espacio con el nombre '{espacio}'.")
            return queryset

        # Si no se proporcionó el parámetro 'espacio', devuelve todos los objetos
        return UsuarioEspacio.objects.all()

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







