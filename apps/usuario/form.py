from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm (UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels ={
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo',
        }
    
    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })