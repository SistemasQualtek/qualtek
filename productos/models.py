# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import os
from django.db import models

# Create your models here.
def get_filename_ext(filepath):
    nombre_base = os.path.basename(filepath)
    nombre, ext = os.path.splitext(nombre_base)
    return nombre, ext

def upload_image_pathb(instancia, nombrearchivo):
    # print(instancia)
    # print(nombrearchivo)
    nuevo_nombrearchivo = random.randint(1,3910209312)
    nombre, ext = get_filename_ext(nombrearchivo)
    nombrearchivo_final = '{nuevo_nombrearchivo}{ext}'.format(nuevo_nombrearchivo=nuevo_nombrearchivo,ext=ext)
    return "almacen/c-b/{nuevo_nombrearchivo}/{nombrearchivo_final}".format(
            nuevo_nombrearchivo=nuevo_nombrearchivo,
            nombrearchivo_final=nombrearchivo_final
            )

def upload_image_path(instancia, nombrearchivo):
    print(instancia)
    print(nombrearchivo)
    nuevo_nombrearchivo = random.randint(1,3910209312)
    nombre, ext = get_filename_ext(nombrearchivo)
    nombrearchivo_final = '{nuevo_nombrearchivo}{ext}'.format(nuevo_nombrearchivo=nuevo_nombrearchivo,ext=ext)
    return "almacen/miniaturas/{nuevo_nombrearchivo}/{nombrearchivo_final}".format(
            nuevo_nombrearchivo=nuevo_nombrearchivo,
            nombrearchivo_final=nombrearchivo_final
            )


class Log(models.Model):
    fecha = models.DateField(auto_now_add=True)
    producto = models.ForeignKey('Producto', null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    culpable = models.CharField(max_length=50, blank=True, null=True)
    ilicito = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.producto

class Proveedor(models.Model):
	proveedor = models.CharField(max_length=255)

	def __str__(self):
		return self.proveedor


class Producto(models.Model):
    codigo = models.BigIntegerField(null=True, blank=True, unique=True)
    descripcion = models.CharField(max_length=255, blank=True,null=True)
    unidad = models.CharField(max_length=50,blank=True,null=True)
    medida = models.CharField(max_length=50,blank=True,null=True)
    existencia = models.IntegerField(null=True, blank=True)
    proveedor = models.CharField(max_length=255, blank=True,null=True)
    cantidad_caja = models.IntegerField(blank=True, null=True)
    cantidad_rb = models.IntegerField(blank=True, null=True)
    ubicacion = models.CharField(max_length=50,blank=True,null=True)
    costo = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=5)
    precio = models.DecimalField(max_digits=9,decimal_places=3, null=True, blank=True)
    release = models.BooleanField(default=False)
    def __str__(self):
        return self.descripcion
