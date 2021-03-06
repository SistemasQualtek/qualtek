# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-23 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_remove_cliente_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='empresa',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
