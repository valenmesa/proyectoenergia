from django.shortcuts import render
from django.http import HttpResponse
from apps.cliente.models import Cliente
from apps.cliente.form import ClienteForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.
#Pagina inicial
def index(request):
    return render(request, "profesor/index.html")

class ClienteList(LoginRequiredMixin, generic.ListView):
    model=Cliente
    template_name='cliente/cliente_list.html'
    context_object_name="obj"
    login_url="login"

#crear registro
class ClienteCreate(LoginRequiredMixin, generic.CreateView):
    model=Cliente
    form_class= ClienteForm
    template_name='cliente/cliente_form.html'
    success_url= reverse_lazy('cliente_listar')
    context_object_name="obj"
    login_url="login"

    def form_valid(self, form):
        form.instance.uc=self.request.user
        return super().form_valid(form)

#Editar registro
class ClienteEdit(LoginRequiredMixin, generic.UpdateView):
    model=Cliente
    form_class= ClienteForm
    template_name='cliente/cliente_form.html'
    success_url= reverse_lazy('cliente_listar')
    context_object_name="obj"
    login_url="login"

    def form_valid(self, form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)

# Eliminar registro
class ClienteDelete(LoginRequiredMixin, generic.DeleteView):
    model=Cliente
    template_name='cliente/cliente_delete.html'
    success_url= reverse_lazy('cliente_listar')
    context_object_name="obj"

