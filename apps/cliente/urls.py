from  django.urls import re_path, include
from apps.cliente.views import index, ClienteList, ClienteCreate, ClienteEdit, ClienteDelete

urlpatterns = [
    # re_path(r'^$', index, name='index'),
    re_path(r'^editar/(?P<pk>\d+)/$', ClienteEdit.as_view(), name='cliente_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', ClienteDelete.as_view(), name='cliente_eliminar'),
    re_path(r'^nuevo$', ClienteCreate.as_view(), name='cliente_crear'),
    re_path(r'^listar$', ClienteList.as_view(), name='cliente_listar'),
]