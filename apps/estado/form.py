from django import forms
from apps.estado.models import Estado

class EstadoForm (forms.ModelForm):
    class Meta:
        model = Estado
        fields = [
            'descripcion_estado',
        ]
        labels ={
            'descripcion_estado': 'Descripcion',
        }
        widgets={
            'descripcion_estado': forms.TextInput(attrs={'class':'form-control'}),
        }
