from  django.urls import re_path, include, path
from apps.cliente.views import index, ClienteList, ClienteCreate, ClienteEdit, ClienteInactivar

urlpatterns = [
    # re_path(r'^$', index, name='index'),
    re_path(r'^editar/(?P<pk>\d+)/$', ClienteEdit.as_view(), name='cliente_editar'),
    path(r'cliente/inactivar/<int:id>', ClienteInactivar, name='cliente_inactivar'),
    re_path(r'^nuevo$', ClienteCreate.as_view(), name='cliente_crear'),
    re_path(r'^listar$', ClienteList.as_view(), name='cliente_listar'),
]