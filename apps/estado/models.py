from django.db import models

# Create your models here.

#Modelo Documento
class Estado(models.Model):
    descripcion_estado=models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.descripcion_estado)