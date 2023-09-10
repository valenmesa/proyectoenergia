from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pedido, Compras
from .form import PedidoForm
from apps.servicios.models import servicios
from django.urls import reverse_lazy
from django.db.models import Sum
import json
import datetime

# Create your views here.

class PedidoView(LoginRequiredMixin, generic.ListView):
    model=Pedido
    template_name="pedido/pedido_list.html"
    context_object_name="obj"
    login_url="login"

def pedidos(request, compra_id=None):
    template_name="pedido/compras.html"
    servicios_list=servicios.objects.filter(estado=True)
    form_pedido={}
    contexto={}

    if request.method=='GET':
        form_pedido=PedidoForm()
        ped = Pedido.objects.filter(pk=compra_id).first()

        if ped:
            det = Compras.objects.filter(compra=ped)
            fecha_factura=datetime.date.isoformat(ped.fecha_factura)


            # fecha_compra=datetime.strptime(ped.fecha_compra, '%Y-%m-%d').strftime('%m/%d/%Y')
            fecha_factura=datetime.strptime(ped.fecha_factura, '%Y-%m-%d').strftime('%m/%d/%Y')
            e = {
                'fecha_factura': fecha_factura,
                'cliente':ped.Cliente,
                'observacion':ped.observacion,
                'sub_total': ped.sub_total,
                'iva': ped.iva,
                'total_compra': ped.total_compra
            }
            form_pedido=PedidoForm(e)
        else:
            det=None
        contexto={'pedido': ped, 'compras':det, 'form_ped':form_pedido}

    if request.method=='POST':

        fecha_factura=request.POST.get("fecha_factura")
        Cliente=request.POST.get("cliente")
        observacion=request.POST.get("observacion")
        sub_total=0
        iva=0
        total_compra=0

        if not compra_id:
            cliente=Cliente.objects.get(pk=Cliente)

            ped= Pedido(
                fecha_factura=fecha_factura,
                cliente=Cliente,
                observacion=observacion,
            )

            if ped:
                ped.save()
                compra_id=ped.id
        else:
            ped=Pedido.objects.filter(pk=compra_id).first()
            if ped:
                ped.fecha_factura=fecha_factura
                ped.observacion=observacion
                ped.save()

        if not compra_id:
            return redirect("pedido: compras_list")
        servicio=request.POST.get("id_servicio")
        cantidad=request.POST.get("id_cantidad_compras")
        precio=request.POST.get("id_precio_compras")
        sub_total_compras=request.POST.get("id_sub_total_compras")
        iva_compras=request.POST.get("id_iva_compras")
        total_compra_compras=request.POST.get("id_total_compra_compras")

        servicios_list=servicios.objects.get(pk=servicios)

        det=Compras(
            compra=ped,
            servicios=servicios_list,
            cantidad=cantidad,
            precio_prv=precio,
            iva=iva_compras,
        )
        if det:
            det.save()
            sub_total=Compras.objects.filter(compra=compra_id).aggregate(Sum('sub_total'))
            iva=Compras.objects.filter(compra=compra_id).aggregate(Sum('iva'))
            ped.sub_total=sub_total["sub_total__sum"]
            ped.iva=iva["iva__sum"]
            ped.save()

        return redirect("pedido:pedido_editar", compra_id=compra_id)

    return render(request, template_name, contexto)

class ComprasDelete(LoginRequiredMixin, generic.DeleteView):
    model=Compras
    template_name="pedido/compras_del.html"
    context_object_name="obj"
    
    def get_success_url(self):
        compra_id=self.kwargs['compra_id']
        return reverse_lazy('pedido:pedido_editar', kwargs={'compra_id': compra_id})