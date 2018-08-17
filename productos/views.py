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
    tubow = Producto.objects.filter(proveedor='Tubo W').order_by('medida').values('medida')
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
        'count':count,
        'tubow':tubow,

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
    fields = ['codigo', 'descripcion','medida','unidad', 'proveedor','ubicacion', 'existencia', 'costo','precio', 'release']
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

####################################### ahuevo ################################

def pdftwm(request):
    # print "Genero el PDF Ventas del Dia"
    date = request.GET.get('date','2017-05-04')
    medida = request.GET.get('medida','2017-05-04')
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Tubo_W_con_Medida_de_"+medida+".pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    courses = []
    styles = getSampleStyleSheet()
    header = Paragraph("Tubo W de "+medida, styles['Title'])
    courses.append(header)
    headings = ('Codigo', 'Descripcion', 'Medida', 'Existencia')
    allcourses = [(p.codigo, p.descripcion, p.medida, p.existencia) for p in Producto.objects.filter(medida = medida).order_by('descripcion')]
    t = Table([headings] + allcourses)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.white)
        ]
    ))

    courses.append(t)
    doc.build(courses)
    response.write(buff.getvalue())
    buff.close()
    return response
####################################### ahuevo ################################

####################################### Proveedores Pedidos ########################
def PedidosList(request):
    count = Producto.objects.count()
    productos = Producto.objects.order_by('id')
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            producto.save()
            return HttpResponseRedirect('/Lista/Pedidos/')
    else:
        form = ProductoForm()
    template = loader.get_template('productos/pedidos_list.html')
    context = {
        'productos':productos,
        'form':form,
        'count':count

    }
    # print (productos)
    return render(request, 'productos/pedidos_list.html', context)


################################## Proveedor #######################################
def ProveedorList(request):
    count = Proveedor.objects.count()
    proveedor = Proveedor.objects.order_by('id')
    if request.method == 'POST':
        form = ProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            producto.save()
            return HttpResponseRedirect('/Lista/Proveedores/')
    else:
        form = ProveedorForm()
    template = loader.get_template('proveedores/proveedor_list.html')
    context = {
        'proveedor':proveedor,
        'form':form,
        'count':count

    }
    # print (productos)
    return render(request, 'proveedores/proveedor_list.html', context)

def ProveedorDetail(request,pk):
    elculodealberto = get_object_or_404(Proveedor, pk=pk)
    template = loader.get_template('proveedores/proveedor_detail.html')
    context = {
    'elculodealberto':elculodealberto
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(reverse('proveedores/proveedor_detail.html', args=(elculodealberto.id,)))
