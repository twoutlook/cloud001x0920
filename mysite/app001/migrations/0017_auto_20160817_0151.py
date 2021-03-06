# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0016_auto_20160817_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item003',
            name='field2',
        ),
        migrations.RemoveField(
            model_name='item003',
            name='field4',
        ),
        migrations.RemoveField(
            model_name='item003',
            name='field5',
        ),
        migrations.RemoveField(
            model_name='item003',
            name='id',
        ),
        migrations.AddField(
            model_name='item003',
            name='field1a',
            field=models.CharField(default='.', max_length=200, verbose_name='噸位'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2a1',
            field=models.CharField(default='.', max_length=200, verbose_name='格林柱'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2a2',
            field=models.CharField(default='.', max_length=200, verbose_name='機架底座'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2a3',
            field=models.CharField(default='.', max_length=200, verbose_name='模板'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2a4',
            field=models.CharField(default='.', max_length=200, verbose_name='合模'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2a5',
            field=models.CharField(default='.', max_length=200, verbose_name='間隙'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2a6',
            field=models.CharField(default='.', max_length=200, verbose_name='膜厚調節'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2b1',
            field=models.CharField(default='.', max_length=200, verbose_name='油管'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2b2',
            field=models.CharField(default='.', max_length=200, verbose_name='過濾'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2b3',
            field=models.CharField(default='.', max_length=200, verbose_name='油箱'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2b4',
            field=models.CharField(default='.', max_length=200, verbose_name='馬達'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2c1',
            field=models.CharField(default='.', max_length=200, verbose_name='潤滑'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2d1',
            field=models.CharField(default='.', max_length=200, verbose_name='氮氣'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2e1',
            field=models.CharField(default='.', max_length=200, verbose_name='電控'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2f1',
            field=models.CharField(default='.', max_length=200, verbose_name='自動噴霧'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2g1',
            field=models.CharField(default='.', max_length=200, verbose_name='自動取出'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field2h1',
            field=models.CharField(default='.', max_length=200, verbose_name='自動切邊去毛'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field4a',
            field=models.CharField(default='.', max_length=200, verbose_name='進度一'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field4b',
            field=models.CharField(default='.', max_length=200, verbose_name='進度二'),
        ),
        migrations.AddField(
            model_name='item003',
            name='field4c',
            field=models.CharField(default='.', max_length=200, verbose_name='進度三'),
        ),
        migrations.AlterField(
            model_name='item003',
            name='field1',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='壓鑄機編號'),
        ),
        migrations.AlterField(
            model_name='item003',
            name='field3',
            field=models.CharField(default='.', max_length=200, verbose_name='零件'),
        ),
    ]
