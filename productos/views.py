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
            return HttpResponseRedirect('productos/producto_list.html')
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
        venta = Log()
        producto.existencia = producto.existencia - cantidad
        venta.producto = producto
        venta.cantidad = cantidad
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
        venta = Log()
        producto.existencia = producto.existencia + cantidad
        venta.producto = producto
        venta.cantidad = cantidad
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
    log = Venta.objects.filter(fecha= time.strftime("%Y-%m-%d"))
    template = loader.get_template('productos/venta_list.html')
    context = {
        'playera': playera
    }
    return HttpResponse(template.render(context, request))


def pdfgen(request):
    # print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Stock.pdf"  # llamado clientes
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
    header = Paragraph("Reporte General de Almacen.", styles['Title'])
    header.hAlign = 'CENTER'
    courses.append(header)
    headings = ('Código', 'Descripción','Medida','Unidad', 'Existencia', 'Proveedor')
    allcourses = [(p.codigo, p.descripcion, p.medida, p.unidad, p.existencia, p.proveedor) for p in Producto.objects.all().order_by('proveedor', 'medida')]
    # print allcourses
    t = Table([headings] + allcourses)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (5, -1), 1, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            ('ALIGN',(0,0),(3,0),'CENTER'),
        ]
    ))

    courses.append(t)
    doc.build(courses)
    response.write(buff.getvalue())
    buff.close()
    return response


def pdfrel(request):
    # print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Release.pdf"  # llamado clientes
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
    header = Paragraph("Release", styles['Title'])
    header.Align = 'CENTER'
    courses.append(header)
    headings = ('Código', 'Descripción', 'Existencia', 'Proveedor')
    allcourses = [(p.codigo, p.descripcion, p.existencia, p.proveedor) for p in Producto.objects.all().filter(release=True).order_by('id')]
    # print allcourses
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


def pdfdia(request):
    # print "Genero el PDF Ventas del Dia"
    date = request.GET.get('date','2017-05-04')
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Reporte del Día "+date+".pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
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
    header = Paragraph("Reporte de Ventas de "+date, styles['Title'])
    courses.append(header)
    headings = ('Id', 'Producto', 'Cantidad Vendida','Subtotal')
    allcourses = [(p.id, p.producto, p.cantidad,(p.producto.precio*p.cantidad)) for p in Venta.objects.filter(fecha = date)]
    totalfinal = 0
    saldos = 0
    for p in Venta.objects.filter(fecha = date):
        saldos = saldos + p.cantidad
        totalfinal = totalfinal + (p.producto.precio*p.cantidad)
        # print (saldos)
    total = ('','Total', saldos, totalfinal)
    # print allcourses

    allcourses.append(total)
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

def grafica_pastel(request):
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Gráfica.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()

    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=200,
                            bottomMargin=18,
                            )
    story = []
    estilo = getSampleStyleSheet()


    d = Drawing(300, 200)
    pc = Pie()
    pc.x = 65
    pc.y = 15
    pc.width = 170
    pc.height = 170
    # pc.data = [11,20,30,40,50]
    # pc.labels = ['IE','Kopete','Chrome','Firefox','Opera']
    datos = []
    etiquetas = []

    for key in Venta.objects.values('producto').annotate(suma=Sum('cantidad')):
        producto = get_object_or_404(Producto, pk=key['producto'])
        etiquetas.append(producto.nombre)
        datos.append(key['suma'])
    pc.data = datos
    pc.labels = etiquetas

    pc.slices.strokeWidth=0.5
    pc.slices[3].popout = 10
    pc.slices[3].strokeWidth = 2
    pc.slices[3].strokeDashArray = [2,2]
    pc.slices[3].labelRadius = 1.75
    pc.slices[3].fontColor = colors.red
    pc.sideLabels = 1  # Con 0 no se muestran lÌneas hacia las etiquetas
    #~ pc.slices.labelRadius = 0.65  # Para mostrar el texto dentro de las tajadas

    #Insertamos la legenda

    legend = Legend()
    legend.x               = 370
    legend.y               = 0
    legend.dx              = 8
    legend.dy              = 8
    legend.fontName        = 'Helvetica'
    legend.fontSize        = 7
    legend.boxAnchor       = 'n'
    legend.columnMaximum   = 10
    legend.strokeWidth     = 1
    legend.strokeColor     = colors.black
    legend.deltax          = 75
    legend.deltay          = 10
    legend.autoXPadding    = 5
    legend.yGap            = 0
    legend.dxTextSpace     = 5
    legend.alignment       = 'right'
    legend.dividerLines    = 1|2|4
    legend.dividerOffsY    = 4.5
    legend.subCols.rpad    = 30

    #Insertemos nuestros propios colores
    colores  = [colors.blue, colors.red, colors.green, colors.yellow, colors.pink]
    for i, color in enumerate(colores):
        pc.slices[i].fillColor = color

    legend.colorNamePairs  = [(
                                pc.slices[i].fillColor,
                                (pc.labels[i][0:20], '%0.2f' % pc.data[i])
                               ) for i in xrange(len(pc.data))]

    d.add(pc)
    d.add(legend)
    story.append(d)
    doc.build(story)
    response.write(buff.getvalue())
    buff.close()
    return response

################################################## EXCEL Reporte ##########################################################
class ReporteQualtekExcel(TemplateView):
    def get(self, request, *args, **kwargs):
        conta = Producto.objects.all().order_by('proveedor','medida')
        wb = Workbook()
        ws = wb.active
        ws['A1'] = 'Código'


        ws['B1'] = 'Descripcion'
        ws['C1'] = 'Unidad'
        ws['D1'] = 'Medida'
        ws['E1'] = 'Existencia'
        ws['F1'] = 'Proveedor'
        ws['G1'] = 'Cantidad x Caja'
        ws['H1'] = 'Cantidad x Rollo/Bolsa'
        ws['I1'] = 'Ubicacion'
        ws['J1'] = 'Costo'
        ws['K1'] = 'Precio'
        ws['L1'] = 'Release'
        cont=2

        for con in conta:
            ws.cell(row=cont,column=1).value = con.codigo
            ws.cell(row=cont,column=2).value = con.descripcion
            ws.cell(row=cont,column=3).value = con.unidad
            ws.cell(row=cont,column=4).value = con.medida
            ws.cell(row=cont,column=5).value = con.existencia
            ws.cell(row=cont,column=6).value = con.proveedor
            ws.cell(row=cont,column=7).value = con.cantidad_caja
            ws.cell(row=cont,column=8).value = con.cantidad_rb
            ws.cell(row=cont,column=9).value = con.ubicacion
            ws.cell(row=cont,column=10).value = con.costo
            ws.cell(row=cont,column=11).value = con.precio
            ws.cell(row=cont,column=12).value = con.release
            cont = cont + 1

        nombre_archivo ="AlmacenExcel.xlsx"
        response = HttpResponse(content_type="application/ms-excel")
        contenido = "attachment; filename={0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        wb.save(response)
        return response
################################################## EXCEL Reporte ##########################################################
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
