from django.db import models

# Create your models here.
class Usuarios (models.model): 
    mombre=models.TextField("nombre")
    apellidos=models.TextField("apellidos")
    rol_id=models.TextField("rol_id")