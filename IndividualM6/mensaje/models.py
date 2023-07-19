from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Publicacion(models.Model):
    nombre = models.CharField(max_length=254)
    edad = models.IntegerField()
    correo = models.EmailField(max_length=254)
    telefono = models.TextField()
    direccion = models.CharField(max_length=254)


class Tweet(models.Model):
    cuerpo = models.TextField(max_length=250)
    fecha = models.DateTimeField(default= timezone.now)
# Create your models here.

# Create your models here.
