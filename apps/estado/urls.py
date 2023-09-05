from  django.urls import re_path, include
from apps.estado.views import index, EstadoList, EstadoCreate, EstadoEdit, EstadoDelete

urlpatterns = [
    # re_path(r'^$', index, name='index'),
    re_path(r'^editar/(?P<pk>\d+)/$', EstadoEdit.as_view(), name='estado_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', EstadoDelete.as_view(), name='estado_eliminar'),
    re_path(r'^nuevo$', EstadoCreate.as_view(), name='estado_crear'),
    re_path(r'^listar$', EstadoList.as_view(), name='estado_listar'),
]