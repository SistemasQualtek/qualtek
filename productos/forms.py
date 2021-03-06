# This Python file uses the following encoding: utf-8
from django import forms
from .models import Producto, Proveedor, Log
from django.forms import ModelForm, Textarea, DateInput, TextInput, NumberInput, SelectDateWidget, CheckboxInput, Select
choicestxt=(('---------','---------'),('Tubo W','Tubo W'),('Tubo Qualtek','Tubo Qualtek'),('Qualtek','Qualtek'),('Varios','Varios'))
choicesUNI=(('---------','---------'),('METRO','METRO'), ('PZA','PZA'))
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
            'precio':'Precio',
            'release':'Release'
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
            'unidad': forms.Select(attrs={
                'id': 'unidad',
                'class':'form-control',
                'name': 'unidad',
                },choices=choicesUNI),
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
            'proveedor': forms.Select(attrs={
                'id': 'proveedor',
                'class':'form-control',
                'name': 'proveedor',
                },choices=choicestxt),
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
            'release':  CheckboxInput(attrs={
                'class':'checkbox',
                'id': 'release',
                'name': 'release',
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
            'cantidad_vendida': NumberInput(attrs={'value': 0}),
            'culpable': TextInput(attrs={
                'class':'form-control',
                'id': 'culpable',
                'name': 'culpable',
                'placeholder':'La última que te veo......'
                }),
            'ilicito': TextInput(attrs={
                'class':'form-control',
                'id': 'ilicito',
                'name': 'ilicito',
                'placeholder':'Ahora si ya mamastemprano......'
                }),
        }
