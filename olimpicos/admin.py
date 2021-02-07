from django.contrib import admin

# Register your models here.

from .models import (
    Modalidad, Deporte, Deportista, Evento, Estudiante, Participacion
)

admin.site.register(Modalidad)
admin.site.register(Deporte)
admin.site.register(Deportista)
admin.site.register(Evento)
admin.site.register(Estudiante)
admin.site.register(Participacion)