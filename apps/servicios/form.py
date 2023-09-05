from django import forms
from apps.servicios.models import servicios

class serviciosForm (forms.ModelForm):
    class Meta:
        model = servicios
        fields = [
            'Nombre_Servicio',
            'Descripcion_Servicio',
            'Valor_Servicio',
            'estado',
        ]
        labels={
            'Nombre_Servicio':'Nombre',
            'Descripcion_Servicio':'Descripcion',
            'Valor_Servicio':'Valor',
            'estado': 'Estado',
        }
        widgets={
            'Nombre_Servicio':forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion_Servicio':forms.Textarea(attrs={'class':'form-control'}),
            'Valor_Servicio':forms.TextInput(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **Kwargs):
                super().__init__(*args, **Kwargs)
                for field in iter(self.fields):
                    self.fields[field].widget.attrs.update({
                        'class':'form-control'
                    })

                self.fields['estado'] = forms.BooleanField()