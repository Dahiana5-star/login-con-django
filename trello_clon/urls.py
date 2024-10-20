"""
URL configuration for trello_clon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views


# Creamos el router
router = DefaultRouter()

# Registramos los ViewSets en el router
router.register(r'users', views.UserViewSet)
router.register(r'tarjetas', views.TarjetaViewSet)
router.register(r'usuarioTarjetas', views.UsuarioTarjetaViewSet)
router.register(r'estadoEspacios', views.EstadoEspacioViewSet)
router.register(r'espacios', views.EspacioViewSet)
router.register(r'usuarioEspacios', views.UsuarioEspacioViewSet)
router.register(r'tableros', views.TableroViewSet)
router.register(r'estados', views.EstadoViewSet)
router.register(r'estadoTarjetas', views.EstadoTarjetaViewSet)
router.register(r'subtareas', views.SubtareaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Rutas de la app users
    path('api/', include(router.urls)),

]






