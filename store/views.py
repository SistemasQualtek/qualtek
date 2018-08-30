#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout, get_user_model
from productos.models import Producto, Proveedor, Log
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from clientes.models import Venta
from .forms import ContactoForm, LoginForm, RegisterForm
import datetime
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.detail import DetailView
from datetime import date


import time
User = get_user_model()

class AuthDetail(DetailView):
    model = User
    fields = ['id','username', 'password', 'first_name','last_name','last_login','is_active','is_staff','is_superuser']
class AuthUpdate(UpdateView):
    model = User
    success_url = reverse_lazy('users')
    fields = ['id','username', 'first_name','last_name','email','is_active','is_superuser','is_staff']
class AuthDelete(DeleteView):
    model = User
    success_url = reverse_lazy('users')

def home_page(request):
    count = Producto.objects.count()
    countw = Producto.objects.filter(proveedor='Tubo W').count()
    countq = Producto.objects.filter(proveedor='Tubo Qualtek').count()
    countv = Producto.objects.filter(proveedor='Varios').count()
    countqk = Producto.objects.filter(proveedor='Qualtek').count()
    countcyg = Producto.objects.filter(proveedor='Tubo CYG').count()
    countiewc = Producto.objects.filter(proveedor='Tubo IEWC').count()
    today = time.strftime("%Y-%m-%d")
    mes = time.strftime("%Y-%m")
    ent_hoy = Venta.objects.filter(estado='Generada', fecha_entrega = today).order_by('fecha_entrega')
    ent_ayer = Venta.objects.filter(estado='Generada', fecha_entrega__icontains = '2018-11').order_by('fecha_entrega')
    ent_manana = Venta.objects.filter(estado='Generada').order_by('fecha_entrega')
    usuario = User
    context = {
        'countv':countv,
        'countq':countq,
        'countw':countw,
        'countcyg':countcyg,
        'countiewc':countiewc,
        'countqk':countqk,
        'count':count,
        "title":"Inicio",
        "content": "Welcome to home page",
        'ent_hoy':ent_hoy,
        'ent_ayer':ent_ayer,
        'ent_manana':ent_manana,
        'today':today
        # "queryseto": queryseto

    }
    return render(request, "home_page.html", context)

def reportes(request):
    return render(request, "reportes/reportes.html")

def contact_page(request):
    form = ContactoForm(request.POST or None)
    context = {
        "title":"Contacto",
        "content": "Welcome to contact page",
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"Acerca de",
        "content": "Welcome to about page"
    }
    return render(request, "home_page.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("usuario")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            # context['form'] = LoginForm()
            return redirect("/")
            print(request.user.is_authenticated())
        else:
            print("error")
    return render(request, "auth/login.html",context)



def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        usuario_nuevo = User.objects.create_user(username,email,password)
        messages.info(request, 'Usuario Registrado Exitosamente!')
        print(usuario_nuevo)
    return render(request, "auth/register.html",context)

def lista_de_usuarios(request):
    queryset = User.objects.all().order_by('id')
    context = {
        'queryset':queryset
    }
    return render(request, "auth/list.html",context)
