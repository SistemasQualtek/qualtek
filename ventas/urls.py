from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    VentaUpdate,
    VentaDelete,
    VentaDetail,
)
urlpatterns = [
    url(r'^Ventas/Bitacora/',login_required(views.VentaList), name='ventas_list'),
    url(r'^Ventas/(?P<pk>[0-9]+)/$',views.VentaDetail,name='ventas_detail'),
    url(r'^Ventas/(?P<pk>\d+)', login_required(VentaUpdate.as_view()), name='ventasedit'),
    url(r'^Borrar/(?P<pk>\d+)', login_required(VentaDelete.as_view()), name='ventas_delete'),
]
