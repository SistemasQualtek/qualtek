from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    ClienteList,
    ClienteDetail,
    ClienteCreation,
    ClienteUpdate,
    ClienteDelete,
    VentaUpdate,
    VentaDelete,
    ProCliUpdate,
    ProCliDelete
)
urlpatterns = [
    url(r'^ClienteList/$', ClienteList,name='list_cliente'),
    url(r'^Cliente/Detalle/(?P<pk>[0-9]+)/$', views.ClienteDetail, name='detail_cliente'),
    url(r'^Nuevo/Cliente/',views.cliente,name="cliente"),
    url(r'^Editar/Cliente/(?P<pk>\d+)', login_required(ClienteUpdate.as_view()), name='edit_cliente'),
    url(r'^Borrar/Cliente/(?P<pk>\d+)', login_required(ClienteDelete.as_view()), name='delete_cliente'),
    ############################### Ventas ############################################################
    url(r'^Ventas/Bitacora/',login_required(views.VentaList), name='ventas_list'),
    url(r'^OSA/Ventas/(?P<pk>[0-9]+)/$',views.VentaDetail,name='ventas_detail'),
    url(r'^Editar/Venta/(?P<pk>\d+)', login_required(VentaUpdate.as_view()), name='ventasedit'),
    url(r'^Borrar/Venta/(?P<pk>\d+)', login_required(VentaDelete.as_view()), name='ventas_delete'),
    ############################### Producto Cliente ############################################################
    url(r'^Lista/Producto-Cliente/',login_required(views.Producto_ClienteList), name='pro_cli_list'),
    url(r'^Detalle/Producto-Cliente/(?P<pk>[0-9]+)/$',views.Producto_ClienteDetail,name='pro_cli_detail'),
    url(r'^Editar/Producto-Cliente/(?P<pk>\d+)', login_required(ProCliUpdate.as_view()), name='pro_cli_edit'),
    url(r'^Borrar/Producto-Cliente/(?P<pk>\d+)', login_required(ProCliDelete.as_view()), name='pro_cli_delete'),
]
