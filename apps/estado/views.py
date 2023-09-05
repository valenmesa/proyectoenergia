from django.shortcuts import render
from django.http import HttpResponse
from apps.estado.models import Estado
from apps.estado.form import EstadoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.
#Pagina inicial
def index(request):
    return render(request, "profesor/index.html")

class EstadoList(LoginRequiredMixin, generic.ListView):
    model=Estado
    template_name='estado/estado_list.html'
    context_object_name="obj"
    login_url="login"

#crear registro
class EstadoCreate(LoginRequiredMixin, generic.CreateView):
    model=Estado
    form_class= EstadoForm
    template_name='estado/estado_form.html'
    success_url= reverse_lazy('estado_listar')
    context_object_name="obj"
    login_url="login"

    def form_valid(self, form):
        form.instance.uc=self.request.user
        return super().form_valid(form)

#Editar registro
class EstadoEdit(LoginRequiredMixin, generic.UpdateView):
    model=Estado
    form_class= EstadoForm
    template_name='estado/estado_form.html'
    success_url= reverse_lazy('estado_listar')
    context_object_name="obj"
    login_url="login"

    def form_valid(self, form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)

# Eliminar registro
class EstadoDelete(LoginRequiredMixin, generic.DeleteView):
    model=Estado
    template_name='estado/estado_delete.html'
    success_url= reverse_lazy('estado_listar')
    context_object_name="obj"
