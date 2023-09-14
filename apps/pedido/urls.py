from  django.urls import re_path, include, path
from apps.pedido.views import PedidoView, pedidos, ComprasDelete
from .reportes import reporte_compras, imprimir_compra
urlpatterns = [
    path(r'listar/', PedidoView.as_view(), name='pedido_listar'),
    path(r'nuevo/', pedidos, name='pedido_crear'),
    path(r'pedido/editar/<int:compra_id>', pedidos, name='pedido_editar'),
    path(r'pedido/<int:compra_id>/delete/<int:pk>', ComprasDelete.as_view(), name='compras_del'),
    path(r'pedido/listar', reporte_compras, name='pedido_print_all'),
    path(r'pedido/editar/<int:compra_id>/imprimir', imprimir_compra, name='compras_print_one'),
]