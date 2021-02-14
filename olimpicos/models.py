from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.

class Modalidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return 'modalidad: ' + self.nombre

class Deporte(models.Model):
    nombre = models.CharField(max_length=100)
    icono = models.CharField(max_length=200)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE)

    def __str__(self):
        return 'deporte: ' + self.nombre + ' icono: ' + self.icono


class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    video = models.CharField(max_length=200)

    def __str__(self):
        return 'evento: ' + self.nombre + ' video: ' + self.video


class Deportista(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    lugar_nacimiento = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    peso = models.FloatField()
    estatura = models.FloatField()
    entrenador = models.CharField(max_length=100)
    foto = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='static', null=True)

    def __str__(self):
        return 'deportista:' + self.nombre + ' ' + self.apellido


class DeportistaForm(ModelForm):
    class Meta:
        model = Deportista
        fields = ['nombre', 'apellido', 'lugar_nacimiento', 'fecha_nacimiento', 'edad', 'peso', 'estatura', 'entrenador', 'foto', 'image']


class Participacion(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    resultado = models.FloatField()
    deportista = models.ForeignKey(Deportista, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    def __str__(self):
        return 'participacion:' + str(self.fecha) + ' ' + self.deportista.nombre


class Comentario(models.Model):
    contenido = models.CharField(max_length=500)
    fecha = models.TimeField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Comentario: " + self.contenido
