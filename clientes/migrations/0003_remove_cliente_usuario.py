# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-23 13:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20180723_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='usuario',
        ),
    ]
