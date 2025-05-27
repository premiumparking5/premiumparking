from django.db import models

# Create your models here.
class Permisos (models.model):
   editar=models.TextField("editar")  
   eliminar=models.TextField("eliminar") 
   modificar=models.TextField("modificar")
   rol_id=models.TextField("rol_id")
   agregar=models.TextField("agregar")