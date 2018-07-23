"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views
from django.conf.urls.static import static




from .views import home_page, reportes, contact_page, about_page, login_page, register_page, lista_de_usuarios, AuthDetail,AuthDelete,AuthUpdate

urlpatterns = [
    ########################   urls marco   ########################
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page,name='home'),
    url(r'^Reportes/$', reportes,name='reportes'),
    url(r'^contact/$', contact_page,name='contacto'),
    url(r'^about/$', about_page,name='about'),
    url(r'^login/$', login_page,name='login'),
    url(r'^user_list/$', lista_de_usuarios,name='users'),
    url(r'^register/$', register_page,name='register'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^borrar/(?P<pk>\d+)', AuthDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)', AuthDetail.as_view(), name='detail'),
    url(r'^editar/(?P<pk>\d+)', AuthUpdate.as_view(), name='edit'),
    ########################   urls marco   ########################
    url(r'^', include('productos.urls', namespace='almacen')),
    ########################   urls clientes   ########################
    url(r'^', include('clientes.urls', namespace='clientes')),
    ########################   urls reportes   ########################
    url(r'^', include('reportes.urls', namespace='reportes')),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
