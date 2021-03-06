# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Cliente, Venta, Prod_Cli
from .forms import ClienteForm, VentaForm, ProdCliForm
from productos.models import Producto
import pprint
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth import get_user_model
User = get_user_model()

class ClienteList(ListView):
    model = Cliente
    fields = ['id', 'nombre', 'empresa','email','telefono','telefono2']
class ClienteDetail(DetailView):
    model = Cliente
    fields = ['id', 'nombre', 'empresa','email','telefono','telefono2']
class ClienteCreation(CreateView):
    model = Cliente
    success_url = reverse_lazy('clientes:list_cliente')
    fields = ['id', 'nombre', 'empresa','email','telefono','telefono2']
class ClienteUpdate(UpdateView):
    model = Cliente
    success_url = reverse_lazy('clientes:list_cliente')
    fields = ['id', 'nombre', 'empresa','email','telefono','telefono2']
class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:list_cliente')

def principal(request):
    cliente = Cliente.objects.order_by('id')
    template = loader.get_template('home.html')
    context = {
        'cliente': cliente
    }
    return HttpResponse(template.render(context, request))

def cliente(request):
    users = User.objects.all().order_by('id')
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            cliente = form.save()
            cliente.save()
            return HttpResponseRedirect('/ClienteList')
    else:
        form = ClienteForm()
    template = loader.get_template('clientes/nuevo_cliente.html')
    context = {
        'form': form,
        'users': users

    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/ClienteList/')

def ClienteList(request):
    queryset = Cliente.objects.all().order_by('empresa')
    context = {
        'queryset':queryset
    }
    return render(request, "clientes/cliente_list.html",context)

def ClienteDetail(request,pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    querysetc = Cliente.objects.all()
    queryset = Prod_Cli.objects.filter(empresa_cliente=cliente)
    bitacora = Venta.objects.filter(cliente=cliente).order_by('fecha_entrega')
    template = loader.get_template('clientes/cliente_detail.html')
    if request.method == 'POST':
        form = VentaForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            producto.save()
    else:
        form = VentaForm()
        template = loader.get_template('clientes/cliente_detail.html')
    context = {
    'cliente': cliente,
    'bitacora':bitacora,
    'queryset':queryset,
    'querysetc':querysetc,
    'form':form,
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/login')

############################# Ventas ##############################

class VentaUpdate(UpdateView):
    model = Venta
    fields = ['paqueteria','cantidad_requerida', 'cantidad_entregada','cantidad_faltante','fecha_entrega','factura', 'observaciones','descontado','estado']
    success_url = reverse_lazy('clientes:ventas_list')

class VentaDelete(DeleteView):
    model = Venta
    fields = ['prdoucto','unidad','oc', 'cliente','no_part_cli', 'paqueteria', 'factura','fecha_pedido','cantidad_requerida','cantidad_entregada','cantidad_faltante','fecha_entrega', 'observaciones', 'estado', 'culpable','frecolector', 'falmacen', 'orden_corte']
    success_url = reverse_lazy('clientes:ventas_list')

def VentaDetail(request,pk):
    venta = get_object_or_404(Venta, pk=pk)
    id = Venta.objects.filter(id = venta.id)
    template = loader.get_template('ventas/venta_detail.html')
    forma = VentaForm(request.POST, request.FILES)
    if forma.is_valid():
        venta2 = Venta()
        venta.save()
        venta2.save()
    context = {
    'forma': forma,
    'venta': venta,
    'id':id
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse('ventas/venta_detail.html', context))


def VentaList(request):
    querysetv = Venta.objects.all().order_by('oc')
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
##################################### Producto Cliente #####################################
class ProCliUpdate(UpdateView):
    model = Prod_Cli
    success_url = reverse_lazy('clientes:pro_cli_list')
    fields = ['producto_cliente', 'empresa_cliente']
class ProCliDelete(DeleteView):
    model = Prod_Cli
    success_url = reverse_lazy('clientes:pro_cli_list')
    fields = ['producto_cliente', 'empresa_cliente']

def Producto_ClienteList(request):
    queryset = Prod_Cli.objects.all().order_by('empresa_cliente')
    producto = Producto.objects.all().order_by('medida').order_by('proveedor')
    cliente = Cliente.objects.all().order_by('empresa')
    if request.method == 'POST':
        form = ProdCliForm(request.POST, request.FILES)
        if form.is_valid():
            prod_cli = form.save()
            prod_cli.save()
            return HttpResponseRedirect('/Lista/Producto-Cliente')
    else:
        form = ProdCliForm()
    template = loader.get_template('productos_clientes/prod_cli_list.html')
    context = {
        'queryset':queryset,
        'form':form,
        'producto':producto,
        'cliente':cliente
    }
    return render(request, "productos_clientes/prod_cli_list.html",context)

def Producto_ClienteDetail(request,pk):
    producto_cliente = get_object_or_404(Prod_Cli, pk=pk)
    template = loader.get_template('productos_clientes/prod_cli_detail.html')
    context = {
    'producto_cliente':producto_cliente
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/login')
