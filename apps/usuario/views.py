from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from apps.usuario.form import RegistroForm

from django.urls import reverse_lazy

# Create your views here.
class RegistroUsuario(CreateView):
    model=User
    form_class= RegistroForm
    template_name='usuario/registrar.html'
    success_url= reverse_lazy('profesor_listar')