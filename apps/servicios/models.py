from django.db import models

# Create your models here.

class servicios(models.Model):
    Nombre_Servicio=models.CharField(max_length=100)
    Descripcion_Servicio=models.TextField()
    Valor_Servicio=models.BigIntegerField()
    estado=models.BooleanField(default=True)
    def __str__(self):
        return '{} {}'.format(self.Nombre_Servicio)