from django.shortcuts import render
from django.http import HttpResponse
from apps.servicios.models import servicios
from apps.servicios.form import serviciosForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.
def index(request):
    return HttpResponse('Index servicio')


class serviciosList(LoginRequiredMixin, generic.ListView):
    model=servicios
    template_name='servicios/servicios_list.html'
    context_object_name="obj"
    login_url="login"

#crear registro
class serviciosCreate(LoginRequiredMixin, generic.CreateView):
    model=servicios
    form_class= serviciosForm
    template_name='servicios/servicios_form.html'
    success_url= reverse_lazy('servicios_listar')
    context_object_name="obj"
    login_url="login"

    def form_valid(self, form):
        form.instance.uc=self.request.user
        return super().form_valid(form)
    
#Editar registro
class serviciosEdit(LoginRequiredMixin, generic.UpdateView):
    model=servicios
    form_class= serviciosForm
    template_name='servicios/servicios_form.html'
    success_url= reverse_lazy('servicios_listar')
    context_object_name="obj"
    login_url="login"

    def form_valid(self, form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)
    
# Inactivar registro
def ServiciosInactivar(request, id):
    template_name="servicios/servicios_inactivar.html"
    contexto={}
    prv=servicios.objects.filter(pk=id).first()
    
    if not prv:
        return HttpResponse("Servicios no existe" + str(id))
    
    if request.method=='GET':
        contexto={'obj': prv}
    
    if request.method=='POST':
        prv.estado=False
        prv.save()
        contexto={'obj': 'OK'}
        return HttpResponse("Servicios Inactivado")

    return render(request, template_name, contexto)
