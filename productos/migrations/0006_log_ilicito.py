# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-16 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20180716_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='ilicito',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]