# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_auto_20161020_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='result',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]