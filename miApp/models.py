from django.db import models

# Create your models here.

class Estadistica(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    fecha_ingreso = models.CharField(max_length=20)    
    hora_ingreso = models.CharField(max_length=10)
    pais = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    tiempo = models.CharField(max_length=20)
    ruta = models.CharField(max_length=200)
    dispositivo = models.CharField(max_length=20)

    def __str__(self):
        return self.id