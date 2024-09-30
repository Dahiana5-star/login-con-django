from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

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