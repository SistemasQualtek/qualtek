#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout, get_user_model
from productos.models import Producto, Proveedor, Log
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
# from productos.models import Perfil, Modelo
from .forms import ContactoForm, LoginForm, RegisterForm
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.detail import DetailView
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
    # queryseto = Modelo.objects.order_by('perfil')[0:1]
    usuario = User
    context = {
        'countv':countv,
        'countq':countq,
        'countw':countw,
        'count':count,
        "title":"Inicio",
        "content": "Welcome to home page",
        # "queryseto": queryseto

    }
    return render(request, "home_page.html", context)

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
