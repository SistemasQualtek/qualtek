# This Python file uses the following encoding: utf-8
from django import forms
from .models import Venta, LogVenta
from django.forms import ModelForm, Textarea, DateInput, TextInput, NumberInput, SelectDateWidget, CheckboxInput, Select
# estado=(('---------','---------'),('Generada','Generada'), ('Armado','Armado'),('Entregado','Entregado'),('Pendiente','Pendiente'))
unidad=(('---------','---------'),('METROS','METROS'), ('PZS','PZS'))
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        labels ={
            'osa':'O. S. A.',
            'factura':'Factura',
            'producto':'Producto',
            'unidad':'Unidad',
            'cliente':'Cliente',
            'fecha_pedido':'Fecha de Pedido',
            'cantidad_requerida':'Cantidad Requerida',
            'fecha_entrega':'Fecha de Entrega',
            'observaciones':'Observaciones',
            'estado':'Estado',
            'culpable':'Culpable',
            'orden_corte':'Orden de Corte',
        }
        widgets = {
            'factura':TextInput(attrs={
                'class':'form-control',
                'id':'factura',
                'name':'factura',
                'placeholder':'Factura'
            }),
            'producto':forms.Select(attrs={
                'class':'form-control',
                'id':'producto',
                'name':'producto',
                'placeholder':'Producto',
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
            'fecha_pedido':SelectDateWidget(),
            'cantidad_requerida':TextInput(attrs={
                'class':'form-control',
                'id':'cantidad_requerida',
                'name':'cantidad_requerida',
                'placeholder':'Cantidad Requerida',
            }),
            'fecha_entrega':SelectDateWidget(),
            'observaciones':Textarea(attrs={
                'class':'form-control',
                'id':'observaciones',
                'name':'observaciones',
                'placeholder':'Observaciones...',
            }),
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
