from django import forms
from apps.cliente.models import Cliente


class ClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre_cliente',
            'apellido_cliente',
            'telefono_cliente',
            'email_cliente',
            'direccion_cliente',
            'tipo_documento',
            'numero_documento',
            'estado',
        ]
        labels = {
            'nombre_cliente': 'Nombre',
            'apellido_cliente': 'Apellido',
            'telefono_cliente': 'Telefono',
            'email_cliente': 'Email',
            'direccion_cliente': 'Direccion',
            'tipo_documento': 'Tipo de documento',
            'numero_documento': 'Numero de documento',
            'estado': 'Estado',
        }
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_cliente': forms.NumberInput(attrs={'class': 'form-control'}),
            'email_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'numero_documento': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **Kwargs):
            super().__init__(*args, **Kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })

            self.fields['estado'] = forms.BooleanField()
