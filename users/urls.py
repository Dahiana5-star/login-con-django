# users/urls.py
from django.urls import path
from .views import RegisterView, loginView, registroView, workspaceView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), # ruta para el registro
    path('login/', obtain_auth_token, name='login'),  # ruta para el login
    path('index/', loginView, name='index'),  # URL para la página de login
    path('registro/', registroView, name='registro'),  # URL para la página de registro
    path('workspace/', workspaceView, name='workspace'),  # URL para la página de workspace
]