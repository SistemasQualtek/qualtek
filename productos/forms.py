# This Python file uses the following encoding: utf-8
from django import forms
from .models import Producto, Proveedor, Log
from django.forms import ModelForm, Textarea, DateInput, TextInput, NumberInput, SelectDateWidget

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        labels ={
            'codigo':'Código',
            'descripcion':'Descripción',
            'unidad':'Unidad',
            'medida':'Medida',
            'existencia':'Existencia',
            'proveedor':'Proveedor',
            'cantidad_caja':'Cantidad (Caja)',
            'cantidad_rb':'Cantidad (Rollo/Bolsa)',
            'ubicacion':'Ubicación',
            'costo':'Costo',
            'barcode':'Código de Barras',
            'precio':'Precio'
        }
        widgets = {
            'codigo': TextInput(attrs={
                'class':'form-control',
                'id': 'codigo',
                'name': 'codigo',
                'placeholder':'Código...'
                }),
            'descripcion': TextInput(attrs={
                'class':'form-control',
                'id': 'descripcion',
                'name': 'descripcion',
                'placeholder':'Descripción...'
                }),
            'unidad': TextInput(attrs={
                'class':'form-control',
                'id': 'unidad',
                'name': 'unidad',
                'placeholder':'0,0'
                }),
            'medida': TextInput(attrs={
                'class':'form-control',
                'id': 'medida',
                'name': 'medida',
                'placeholder':'0,0'
                }),
            'existencia': NumberInput(attrs={
                'class':'form-control',
                'id': 'existencia',
                'name': 'existencia',
                'placeholder':'0,0'
                }),
            'cantidad_caja': NumberInput(attrs={
                'class':'form-control',
                'id': 'cantidad_caja',
                'name': 'cantidad_caja',
                'placeholder':'0,0'
                }),
            'cantidad_rb': NumberInput(attrs={
                'class':'form-control',
                'id': 'cantidad_rb',
                'name': 'cantidad_rb',
                'placeholder':'0,0'
                }),
            'ubicacion': TextInput(attrs={
                'class':'form-control',
                'id': 'ubicacion',
                'name': 'ubicacion',
                'placeholder':'Ubicación...'
                }),
            'costo': NumberInput(attrs={
                'class':'form-control',
                'id': 'costo',
                'name': 'costo',
                'placeholder':'0,0'
                }),
            'precio': NumberInput(attrs={
                'class':'form-control',
                'id': 'precio',
                'name': 'precio',
                'placeholder':'0,0'
                }),
        }



class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = '__all__'
        widgets = {
        	'fecha': SelectDateWidget(),
            'cantidad_vendida': NumberInput(attrs={'value': 0})
        }
