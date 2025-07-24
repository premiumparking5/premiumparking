from django.db import models

# Create your models here.
class Servicios (models.Model): 
    tipo_de_servicio=models.TextField("tipo_de_servicio")
    tiempo_de_servicio=models.TextField("tiempo_de_servicio")
    
