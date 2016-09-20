# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0029_item004v2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item004v2',
        ),
        migrations.AddField(
            model_name='item004',
            name='f01',
            field=models.CharField(default='.', max_length=99, verbose_name='客戶'),
        ),
        migrations.AddField(
            model_name='item004',
            name='f02',
            field=models.CharField(default='.', max_length=99, verbose_name='量產訂單號'),
        ),
        migrations.AddField(
            model_name='item004',
            name='f03',
            field=models.CharField(default='.', max_length=99, verbose_name='產品代碼'),
        ),
        migrations.AddField(
            model_name='item004',
            name='f04',
            field=models.CharField(default='.', max_length=99, verbose_name='產品名稱'),
        ),
        migrations.AddField(
            model_name='item004',
            name='f05',
            field=models.CharField(default='.', max_length=99, verbose_name='計劃交期'),
        ),
        migrations.AddField(
            model_name='item004',
            name='f06',
            field=models.CharField(default='.', max_length=99, verbose_name='訂單量'),
        ),
        migrations.AddField(
            model_name='item004',
            name='f07',
            field=models.CharField(default='.', max_length=99, verbose_name='已交量'),
        ),
        migrations.AddField(
            model_name='item004',
            name='f08',
            field=models.CharField(default='.', max_length=99, verbose_name='未交量'),
        ),
        migrations.AddField(
            model_name='item004',
            name='f09',
            field=models.CharField(default='.', max_length=99, verbose_name='備庫量'),
        ),
        migrations.AddField(
            model_name='item004',
            name='f10',
            field=models.CharField(default='.', max_length=99, verbose_name='欠備庫量'),
        ),
        migrations.AddField(
            model_name='item004',
            name='f11',
            field=models.CharField(default='.', max_length=99, verbose_name='客訴量'),
        ),
        migrations.AddField(
            model_name='item004',
            name='f12',
            field=models.CharField(default='.', max_length=99, verbose_name='模具壽命'),
        ),
    ]
