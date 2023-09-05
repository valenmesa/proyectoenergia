from  django.urls import include, re_path
from apps.usuario.views import RegistroUsuario
# index, UsuarioList, UsuarioEdit, UsuarioDelete

urlpatterns = [
    re_path(r'^nuevo$', RegistroUsuario.as_view(), name='usuario_crear'),
    #re_path(r'^listar$', usuario_list, name='usuario_list'),
    # re_path(r'^editar/(?P<id_usuario>\d+)/$', usuario_edit, name='usuario_editar'),
    # re_path(r'^editar/(?P<pk>\d+)/$', UsuarioEdit.as_view(), name='usuario_editar'),
    # re_path(r'^eliminar/(?P<pk>\d+)/$', UsuarioDelete.as_view(), name='usuario_eliminar'),
    # re_path(r'^listar$', UsuarioList.as_view(), name='usuario_listar'),
]