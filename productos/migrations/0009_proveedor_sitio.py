# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-17 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_auto_20180815_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='sitio',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]