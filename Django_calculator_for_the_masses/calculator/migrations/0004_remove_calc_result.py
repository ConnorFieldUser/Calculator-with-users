# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 22:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_auto_20161019_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calc',
            name='result',
        ),
    ]
