from django.db import models

# Create your models here.
class Rol (models.model):
    nombre = models.TextField("nombres")

    def __str__(self):
        return f'{self.nombre}'