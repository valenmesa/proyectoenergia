from django.db import models

# Create your models here.

#Modelo Documento
class Tipo_Documento(models.Model):
    descripcion=models.CharField(max_length=30)
    def __str__(self):
        return '{}'.format(self.descripcion)

#Modelo Profesor
class Profesor(models.Model):
    #atributos
    nombre_profesor=models.CharField(max_length=50)
    apellido_profesor=models.CharField(max_length=70)
    telefono_profesor=models.CharField(max_length=15)
    email_profesor=models.EmailField()
    direccion_profesor=models.CharField(max_length=40)
    tipo_documento=models.ForeignKey(Tipo_Documento, null=True, blank=True, on_delete=models.CASCADE)
    numero_documento=models.BigIntegerField()
    estado=models.BooleanField(default=True)
    def __str__(self):
        return '{} {}'.format(self.nombre_profesor, self.apellido_profesor)

