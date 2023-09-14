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

# Inactivar registro

def ClienteInactivar(request, id):
    template_name="cliente/cliente_inactivar.html"
    contexto={}
    prv=Cliente.objects.filter(pk=id).first()
    
    if not prv:
        return HttpResponse("Cliente no existe" + str(id))
    
    if request.method=='GET':
        contexto={'obj': prv}
    
    if request.method=='POST':
        prv.estado=False
        prv.save()
        contexto={'obj': 'OK'}
        # return HttpResponse("Cliente Inactivado")

    return render(request, template_name, contexto)
