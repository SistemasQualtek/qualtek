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
    url(r'^Cliente/(?P<pk>[0-9]+)/$', views.ClienteDetail, name='detail_cliente'),
    url(r'^Cliente/nuevo',views.cliente,name="cliente"),
    url(r'^editar_cliente/(?P<pk>\d+)', login_required(ClienteUpdate.as_view()), name='edit_cliente'),
    url(r'^borrar_cliente/(?P<pk>\d+)', login_required(ClienteDelete.as_view()), name='delete_cliente'),
]
