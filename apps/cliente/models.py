from django.db import models
from apps.profesor.models import Tipo_Documento

# Create your models here.

#Modelo cliente
class Cliente(models.Model):
    #atributos
    nombre_cliente=models.CharField(max_length=50)
    apellido_cliente=models.CharField(max_length=70)
    telefono_cliente=models.CharField(max_length=15)
    email_cliente=models.EmailField()
    direccion_cliente=models.CharField(max_length=40)
    tipo_documento=models.ForeignKey(Tipo_Documento, null=True, blank=True, on_delete=models.CASCADE)
    numero_documento=models.BigIntegerField()
    def __str__(self):
        return '{} {}'.format(self.nombre_cliente, self.apellido_cliente)