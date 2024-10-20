from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Tarjeta)
admin.site.register(UsuarioTarjeta)
admin.site.register(EstadoEspacio)
admin.site.register(Espacio)
admin.site.register(UsuarioEspacio)
admin.site.register(Tablero)
admin.site.register(Estado)
admin.site.register(EstadoTarjeta)
admin.site.register(Subtarea)

