# This Python file uses the following encoding: utf-8
from django import forms
from django.forms import TextInput,EmailInput,Select,HiddenInput, Textarea
from .models import Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'empresa', 'direccion', 'email', 'telefono', 'telefono2']
        labels = {
            'nombre' : 'Nombre de Contacto*',
            'empresa' : 'Empresa*',
            'direccion' : 'Dirección*',
            'email' : 'Correo Electrónico*',
            'telefono' : 'Teléfono*',
            'telefono2' : 'Teléfono Adicional',
            }
        widgets = {
            'nombre': TextInput(attrs={
                                    'class':'form-control',
                                    'id': 'nombre_completo',
                                    'name': 'nombre_completo',
                                    'placeholder':'Nombre(s)'
                                    }),
            'empresa': TextInput(attrs={
                                    'class':'form-control',
                                    'id': 'empresa',
                                    'name': 'empresa',
                                    'placeholder':'Empresa'
                                    }),
            'direccion': Textarea(attrs={
                                    'class':'form-control',
                                    'id': 'direccion',
                                    'name': 'direccion',
                                    'placeholder':'Dirección'
                                    }),
            'email': EmailInput(attrs={
                                    'class':'form-control',
                                    'id': 'email',
                                    'name': 'email',
                                    'placeholder':'Correo Electrónico'
                                    }),
            'telefono': TextInput(attrs={
                                    'class':'form-control',
                                    'id': 'telefono',
                                    'name': 'telefono'
                                    }),
            'telefono2': TextInput(attrs={
                                    'class':'form-control',
                                    'id': 'telefono2',
                                    'name': 'telefono2'
                                    }),

                                    }
