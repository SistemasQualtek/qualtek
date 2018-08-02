# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import os
from django.db import models


# Create your models here.
class LogVenta(models.Model):
    osa = models.ForeignKey('Venta', null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    culpable = models.CharField(max_length=50, blank=True, null=True)
    ilicito = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.fecha


class Venta(models.Model):
    osa = models.IntegerField(null=True, blank=True)
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
        return self.osa
