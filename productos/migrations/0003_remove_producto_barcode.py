# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-13 15:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20180713_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='barcode',
        ),
    ]
