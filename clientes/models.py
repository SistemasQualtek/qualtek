# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
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
