from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    ProductoUpdate,
    ProductoDelete,
    Reportar_Pedidos,
)
urlpatterns = [
    url(r'^inicio/',views.inicio, name='inicio'),
    url(r'^Lista/Productos/',login_required(views.ProductoList), name='producto_list'),
    url(r'^Lista/Pedidos/',login_required(views.PedidosList), name='pedidos_list'),
    url(r'^Release/',login_required(views.ReleaseList), name='release'),
    url(r'^Producto/Detalle/(?P<pk>[0-9]+)/$',views.ProductoDetail,name='producto_detail'),
    url(r'^Proveedor/Detalle/(?P<pk>[0-9]+)/$',views.ProveedorDetail,name='proveedor_detail'),
    url(r'^Entrada/(?P<pk>[0-9]+)/$',login_required(views.Entrada),name='padentro'),
    url(r'^Salida/(?P<pk>[0-9]+)/$',login_required(views.Salida),name='pafuera'),
    url(r'^Lista/Proveedor/',login_required(views.ProveedorList), name='proveedor_list'),
    url(r'^Proveedor/Nueva',views.categoria,name="nuevo_proveedor"),
    url(r'^Almacen/Log/',views.Lista_Log,name="log_list"),
    url(r'^PDF/TuboWMedida',login_required(views.pdftwm),name="pdfclitoris"),
    url(r'^Editar/Producto/(?P<pk>\d+)', login_required(ProductoUpdate.as_view()), name='edit'),
    url(r'^Borrar/Producto/(?P<pk>\d+)', login_required(ProductoDelete.as_view()), name='delete'),
    url(r'^XML/Pedidos', login_required(Reportar_Pedidos.as_view()), name="reporteexcelm"),
]
