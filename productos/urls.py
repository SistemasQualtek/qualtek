from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    ProductoList,
    ProductoUpdate,
    ProductoDelete
)
urlpatterns = [
    url(r'^$',views.principal, name='principal'),
    url(r'^inicio/',views.inicio, name='inicio'),
    url(r'^Lista/Productos/',login_required(views.ProductoList), name='producto_list'),
    url(r'^Release/',login_required(views.ReleaseList), name='release'),
    url(r'^Producto/(?P<pk>[0-9]+)/$',views.ProductoDetail,name='producto_detail'),
    url(r'^Entrada/(?P<pk>[0-9]+)/$',login_required(views.Entrada),name='padentro'),
    url(r'^Salida/(?P<pk>[0-9]+)/$',login_required(views.Salida),name='pafuera'),
    url(r'^Proveedor/Nueva',views.categoria,name="nuevo_proveedor"),
    url(r'^Almacen/Log/',views.Lista_Log,name="log_list"),
    url(r'^Pdf/Dia',views.pdfdia,name="pdfdia"),
    url(r'^Pdf/General',login_required(views.pdfgen),name="pdfgen"),
    url(r'^PDF/Grafica',views.grafica_pastel,name="grafica_pastel"),
    url(r'^Editar/(?P<pk>\d+)', login_required(ProductoUpdate.as_view()), name='edit'),
    url(r'^Borrar/(?P<pk>\d+)', login_required(ProductoDelete.as_view()), name='delete'),
]
