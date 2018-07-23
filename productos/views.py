# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Producto, Proveedor, Log
from .forms import ProductoForm, ProveedorForm, LogForm
from django.views.generic.base import TemplateView
import pprint
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
import os
from reportlab.pdfgen import canvas
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from io import BytesIO
from reportlab.lib.colors import PCMYKColor
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.legends import Legend
from django.db.models import Q, Sum
import time
from openpyxl import Workbook


def ProductoList(request):
    count = Producto.objects.count()
    productos = Producto.objects.order_by('id')
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            producto.save()
            return HttpResponseRedirect('/Lista/Productos/')
    else:
        form = ProductoForm()
    template = loader.get_template('productos/producto_list.html')
    context = {
        'productos':productos,
        'form':form,
        'count':count

    }
    # print (productos)
    return render(request, 'productos/producto_list.html', context)

def ProductoDetail(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    template = loader.get_template('productos/producto_detail.html')
    forma = LogForm(request.POST, request.FILES)
    if forma.is_valid():
        cantidad = forma.cleaned_data['cantidad']
        venta = Log()
        producto.existencia = producto.existencia - cantidad
        venta.producto = producto
        venta.cantidad = cantidad
        producto.save()
        venta.save()
    context = {
    'forma': forma,
    'producto': producto
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse('productos/producto_detail.html', args=(producto.id,)))
# Inicio de Salida Manual
def Salida(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    nombre = 'Salida'
    template = loader.get_template('productos/producto_detail.html')
    forma = LogForm(request.POST, request.FILES)
    if forma.is_valid():
        cantidad = forma.cleaned_data['cantidad']
        culpable = forma.cleaned_data['culpable']
        ilicito = forma.cleaned_data['ilicito']
        venta = Log()
        producto.existencia = producto.existencia - cantidad
        venta.producto = producto
        venta.cantidad = cantidad
        venta.culpable = culpable
        venta.ilicito = ilicito
        producto.save()
        venta.save()
    context = {
    'forma': forma,
    'producto': producto,
    'nombre': nombre
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse('productos/producto_detail.html', args=(producto.id,)))
# Fin de Salida Manual

# Inicio de Entrada Manual
def Entrada(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    nombre = 'Entrada'
    template = loader.get_template('productos/producto_detail.html')
    forma = LogForm(request.POST, request.FILES)
    if forma.is_valid():
        cantidad = forma.cleaned_data['cantidad']
        culpable = forma.cleaned_data['culpable']
        ilicito = forma.cleaned_data['ilicito']
        venta = Log()
        producto.existencia = producto.existencia + cantidad
        venta.producto = producto
        venta.cantidad = cantidad
        venta.culpable = culpable
        venta.ilicito = ilicito
        producto.save()
        venta.save()
    context = {
    'forma': forma,
    'producto': producto,
    'nombre': nombre
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse('productos/producto_detail.html', args=(producto.id,)))
# Fin de Entrada Manual

class ProductoUpdate(UpdateView):
    model = Producto
    success_url = reverse_lazy('almacen:producto_list')
    fields = ['codigo', 'descripcion','medida','unidad', 'proveedor', 'existencia', 'costo','precio', 'release']
class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('almacen:producto_list')
    fields = ['codigo', 'descripcion', 'proveedor', 'existencia', 'costo', 'precio']

def principal(request):
    playera = Producto.objects.order_by('id')
    template = loader.get_template('home_page.html')
    context = {
        'playera': playera
    }
    return HttpResponse(template.render(context, request))

def inicio(request):
    playera = Producto.objects.order_by('id')
    template = loader.get_template('inicio.html')
    context = {
        'playera': playera
    }
    return HttpResponse(template.render(context, request))

def producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            producto.save()
            return HttpResponseRedirect('/productos/Lista/Productos/')
    else:
        form = ProductoForm()
    template = loader.get_template('productos/new_producto.html')
    context = {
        'form': form
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('productos:producto_list')

def categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            playera = form.save()
            playera.save()
            return HttpResponseRedirect('/productos/Lista/Productos/')
    else:
        form = CategoriaForm()
    template = loader.get_template('productos/new_categoria.html')
    context = {
        'form': form
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('productos:productos_list')

def Lista_Log(request):
    log = Log.objects.filter(fecha= time.strftime("%Y-%m-%d"))
    template = loader.get_template('productos/venta_list.html')
    context = {
        'log': log
    }
    return HttpResponse(template.render(context, request))


def ReleaseList(request):
    count = Producto.objects.count()
    productos = Producto.objects.order_by('id')
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            producto.save()
            return HttpResponseRedirect('almacen:release')
    else:
        form = ProductoForm()
    template = loader.get_template('productos/release.html')
    context = {
        'productos':productos,
        'form':form,
        'count':count

    }
    # print (productos)
    return render(request, 'productos/release.html', context)
