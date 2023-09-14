from django import forms
from .models import Compras, Pedido

class PedidoForm(forms.ModelForm):
    fecha_factura=forms.DateInput()
    class Meta:
        model = Pedido
        fields = [
            'cliente',
            'fecha_factura',
            'observacion',
            'sub_total',
            'descuento',
            'total_compra',
            'estado_pedido',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        # Hacer que el campo fecha_factura sea de solo lectura
        self.fields['fecha_factura'].widget.attrs['readonly'] = True

        # Hacer que los campos sub_total, descuento y total_compra sean de solo lectura
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['total_compra'].widget.attrs['readonly'] = True

