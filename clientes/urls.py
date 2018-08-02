from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    ClienteList,
    ClienteDetail,
    ClienteCreation,
    ClienteUpdate,
    ClienteDelete
)
urlpatterns = [
    url(r'^ClienteList/$', ClienteList,name='list_cliente'),
    url(r'^Cliente/Detalle/(?P<pk>[0-9]+)/$', views.ClienteDetail, name='detail_cliente'),
    url(r'^Nuevo/Cliente/',views.cliente,name="cliente"),
    url(r'^Editar/Cliente/(?P<pk>\d+)', login_required(ClienteUpdate.as_view()), name='edit_cliente'),
    url(r'^Borrar/Cliente/(?P<pk>\d+)', login_required(ClienteDelete.as_view()), name='delete_cliente'),
]
