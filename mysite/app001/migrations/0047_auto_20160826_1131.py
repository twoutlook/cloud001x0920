# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0046_auto_20160826_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='item008',
            name='data01e_00',
            field=models.NullBooleanField(verbose_name='格林柱-備註說明-正常'),
        ),
        migrations.AddField(
            model_name='item008',
            name='data01e_01',
            field=models.NullBooleanField(verbose_name='格林柱-備註說明-磨損'),
        ),
        migrations.AddField(
            model_name='item008',
            name='data01e_02',
            field=models.NullBooleanField(verbose_name='格林柱-備註說明-無法修復'),
        ),
    ]
