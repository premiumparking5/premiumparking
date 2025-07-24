from django.db import models

# Create your models here.
class Usuarios (models.Model): 
    mombre=models.TextField("nombre")
    apellidos=models.TextField("apellidos")
    rol_id=models.TextField("rol_id")