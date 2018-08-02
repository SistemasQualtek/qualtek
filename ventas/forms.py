# This Python file uses the following encoding: utf-8
from django import forms
from .models import Venta, LogVenta
from django.forms import ModelForm, Textarea, DateInput, TextInput, NumberInput, SelectDateWidget, CheckboxInput, Select
# estado=(('---------','---------'),('Generada','Generada'), ('Armado','Armado'),('Entregado','Entregado'),('Pendiente','Pendiente'))
unidad=(('---------','---------'),('METROS','METROS'), ('PZS','PZS'))
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['osa', 'producto','oc', 'unidad', 'cliente', 'no_part_cli', 'fecha_pedido', 'cantidad_requerida', 'cantidad_entregada', 'cantidad_faltante', 'fecha_entrega', 'estado', 'culpable', 'orden_corte']
        labels ={
            'osa':'Orden de Salida Almacen',
            'producto':'Producto',
            'oc':'Orden de Compra',
            'unidad':'Unidad',
            'cliente':'Cliente',
            'no_part_cli':'No. de Parte del Cliente',
            'fecha_pedido':'Fecha de Pedido',
            'cantidad_requerida':'Cantidad Requerida',
            'cantidad_entregada':'Cantidad Entregada',
            'cantidad_faltante':'Cantidad Faltante',
            'fecha_entrega':'Fecha de Entrega',
            'estado':'Estado',
            'culpable':'Culpable',
            'orden_corte':'Orden de Corte',
        }
        widgets = {
            'osa':TextInput(attrs={
                'class':'form-control',
                'id':'osa',
                'name':'osa',
                'placeholder':'Orden de Salida Almacen'
            }),
            'producto':forms.Select(attrs={
                'class':'form-control',
                'id':'producto',
                'name':'producto',
                'placeholder':'Producto',
            }),
            'oc':TextInput(attrs={
                'class':'form-control',
                'id':'oc',
                'name':'oc',
                'placeholder':'Orden de Compra'
            }),
            'unidad':forms.Select(attrs={
                'class':'form-control',
                'id':'unidad',
                'name':'unidad',
                'placeholder':'Unidad',
            },choices=unidad),
            'cliente':forms.Select(attrs={
                'class':'form-control',
                'id':'cliente',
                'name':'cliente',
            }),
            'no_part_cli':TextInput(attrs={
                'class':'form-control',
                'id':'no_part_cli',
                'name':'no_part_cli',
                'placeholder':'No. de Parte del Cliente',
            }),
            'fecha_pedido':SelectDateWidget(),
            'cantidad_requerida':TextInput(attrs={
                'class':'form-control',
                'id':'cantidad_requerida',
                'name':'cantidad_requerida',
                'placeholder':'Cantidad Requerida',
            }),
            'cantidad_entregada':TextInput(attrs={
                'class':'form-control',
                'id':'cantidad_entregada',
                'name':'cantidad_entregada',
                'placeholder':'Cantidad Entregada ',
            }),
            'cantidad_faltante':TextInput(attrs={
                'class':'form-control',
                'id':'cantidad_faltante',
                'name':'cantidad_faltante',
                'placeholder':'Cantidad Faltante ',
            }),
            'fecha_entrega':SelectDateWidget(),
            'estado': forms.Select(attrs={
                'id': 'estado',
                'class':'form-control',
                'name': 'estado',
                }),
            'culpable':TextInput(attrs={
                'class':'form-control',
                'id':'culpable',
                'name':'culpable',
                'placeholder':'Culpable',
            }),
        }


class LogVentaForm(ModelForm):
    class Meta:
        model = LogVenta
        fields = '__all__'
        widgets = {
            'factura': NumberInput(attrs={'value': 0}),
        	'fecha': SelectDateWidget(),
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
