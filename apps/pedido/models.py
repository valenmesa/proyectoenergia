from django.db import models
from apps.cliente.models import Cliente
from apps.estado.models import Estado
from apps.servicios.models import servicios

# Create your models here.
class Pedido(models.Model):
    fecha_factura=models.DateField(null=True, blank=True)
    observacion=models.TextField(blank=True, null=True)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total_compra=models.FloatField(default=0)
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado_pedido = models.BooleanField(default=True)

    def __str__(self):
        return'{}'.format(self.observacion)

    def save(self, *args, **kwargs):
        self.observacion=self.observacion.lower()
        self.total_compra= self.sub_total - ((float(self.sub_total)*(float(self.descuento)))/100)
        super(Pedido, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Pedidos"
        verbose_name="Pedido"

class Compras(models.Model):
    compra=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    servicios=models.ForeignKey(servicios, on_delete=models.CASCADE)
    cantidad=models.BigIntegerField(default=0)
    precio_prv=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total_compra=models.FloatField(default=0)

    
    def __str__(self):
        return'{}'.fomat(self.servicios)
    
    def save(self):
        self.sub_total=float(float(int(self.cantidad))*float(self.precio_prv))
        self.total_compra=self.sub_total - ((float(self.sub_total)*(float(self.descuento)))/100)
        super(Compras,self).save()
    
    class Meta:
        verbose_name_plural="Detalles Compras"
        verbose_name="Detalle Compra"
