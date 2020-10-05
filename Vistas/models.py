from django.db import models

# Create your models here.
class Persona (models.Model):
	nombre = models.CharField(max_length=30)
	edad = models.IntegerField()
	correo = models.EmailField()
	fecha_n = models.DateField()
	usuario = models.CharField(max_length=40)