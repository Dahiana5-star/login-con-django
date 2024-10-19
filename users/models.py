# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# class Usuario(models.Model):
#     correo = models.EmailField(unique=True)
#     nombre_usuario = models.CharField(max_length=255)
#     contrasena = models.CharField(max_length=255)
#     foto_perfil = models.TextField(null=True, blank=True)
#     fecha_nacimiento = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return self.nombre_usuario

class Tarjeta(models.Model):
    nombre_actividad = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    etiqueta = models.CharField(max_length=255, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    creador_tarjeta = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creador_tarjeta')

    def __str__(self):
        return self.nombre_actividad



class UsuarioTarjeta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    fecha_inicio_asignacion = models.DateTimeField(null=True, blank=True)
    fecha_fin_asignacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = (('usuario', 'tarjeta'))



class EstadoEspacio(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion



class Espacio(models.Model):
    nombre = models.CharField(max_length=255)
    estado = models.ForeignKey(EstadoEspacio, on_delete=models.SET_NULL, null=True)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre



class UsuarioEspacio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    fecha_inicio_asignacion= models.DateTimeField()
    fecha_fin_asignacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = (('usuario', 'espacio'))



class Tablero(models.Model):
    nombre_tablero = models.CharField(max_length=255)
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_tablero



class Estado(models.Model):
    nombre = models.CharField(max_length=255)
    cant_maxima = models.IntegerField()
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE, related_name='tablero_origen')

    def __str__(self):
        return self.nombre



class EstadoTarjeta(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    fecha_inicio_estado = models.DateTimeField()
    fecha_fin_estado = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = (('estado', 'tarjeta'))



class Subtarea(models.Model):
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado_subtarea = models.BooleanField(default=False) 
    fecha_vencimiento = models.DateTimeField()

    def __str__(self):
        return self.descripcion
