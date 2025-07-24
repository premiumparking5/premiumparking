from django.db import models

# Create your models here.
class Vehiculos (models.Model): 
    placa=models.TextField("placa")
    servicio_id=models.TextField("sercicio_id")
    hora_y_fecha_de_enytada=models.TextField("hora_Y_fecha_de_entrada")