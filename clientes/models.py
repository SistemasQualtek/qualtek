# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import os
from productos.models import Producto
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=255,blank=False)
    empresa = models.CharField(max_length=255,blank=False)
    direccion = models.CharField(max_length=255,blank=True)
    email = models.EmailField(max_length=255,blank=False)
    telefono = models.CharField(max_length=255,blank=False)
    telefono2 = models.CharField(max_length=255,blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.empresa

class Prod_Cli(models.Model):
    producto_cliente = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    empresa_cliente = models.ForeignKey('Cliente', null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.producto_cliente



class LogVenta(models.Model):
    producto = models.ForeignKey('Venta', null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    culpable = models.CharField(max_length=50, blank=True, null=True)
    ilicito = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.fecha


class Venta(models.Model):
    producto = models.CharField(max_length=255, null=True, blank=True)
    unidad = models.CharField(max_length=255,default='Metros', null=True, blank=True)
    oc = models.CharField(max_length=255, blank=True, null=True)
    cliente = models.CharField(max_length=255, null=True, blank=True)
    no_part_cli = models.CharField(max_length=255, null=True, blank=True)
    paqueteria = models.CharField(max_length=255, null=True, blank=True)
    factura = models.IntegerField(null=True, blank=True)
    fecha_pedido = models.DateField()
    cantidad_requerida = models.IntegerField()
    cantidad_entregada = models.IntegerField(default=0)
    cantidad_faltante = models.IntegerField(default=0)
    fecha_entrega = models.DateField()
    observaciones = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True, default='Generada')
    culpable = models.CharField(max_length=50, blank=True, null=True)
    frecolector = models.CharField(max_length=255, blank=True, null=True, default='Ventas')
    falmacen = models.CharField(max_length=255, blank=True, null=True, default='Sistemas')
    orden_corte = models.CharField(max_length=255, blank=True, null=True)
    descontado = models.BooleanField(default=False)

    def __str__(self):
        return self.producto
