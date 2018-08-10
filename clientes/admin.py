# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Cliente, Prod_Cli
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id']
    class Meta:
        model = Cliente

admin.site.register(Cliente, ClienteAdmin)

class ProductoClienteAdmin(admin.ModelAdmin):
    list_display = ['id']
    class Meta:
        model = Prod_Cli

admin.site.register(Prod_Cli, ProductoClienteAdmin)
