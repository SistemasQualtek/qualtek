from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Venta
from .forms import VentaForm
from productos.models import Producto
from clientes.models import Cliente
import pprint
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth import get_user_model
User = get_user_model()

class VentaUpdate(UpdateView):
    model = Venta
    fields = ['paqueteria','factura', 'observaciones','descontado','estado']
    success_url = reverse_lazy('ventas:ventas_list')

class VentaDelete(DeleteView):
    model = Venta
    fields = ['oas','prdoucto','unidad','oc', 'cliente','no_part_cli', 'paqueteria', 'factura','fecha_pedido','cantidad_requerida','cantidad_entregada','cantidad_faltante','fecha_entrega', 'observaciones', 'estado', 'culpable','frecolector', 'falmacen', 'orden_corte']
    success_url = reverse_lazy('ventas:ventas_list')

def VentaDetail(request,pk):
    venta = get_object_or_404(Venta, pk=pk)
    osa = Venta.objects.filter(osa = venta.osa)
    template = loader.get_template('ventas/venta_detail.html')
    forma = VentaForm(request.POST, request.FILES)
    if forma.is_valid():
        venta2 = Venta()
        venta.save()
        venta2.save()
    context = {
    'forma': forma,
    'venta': venta,
    'osa':osa
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse('ventas/venta_detail.html', context))

def VentaList(request):
    querysetv = Venta.objects.all().order_by('osa')
    queryset = Producto.objects.all()
    querysetc = Cliente.objects.all()
    if request.method == 'POST':
        form = VentaForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            producto.save()
            return HttpResponseRedirect('/Ventas/Bitacora/')
    else:
        form = VentaForm()
        template = loader.get_template('ventas/venta_list.html')
        context = {
            'form':form,
            'queryset':queryset,
            'querysetc':querysetc,
            'querysetv':querysetv,
            }
        return render(request, 'ventas/venta_list.html', context)
