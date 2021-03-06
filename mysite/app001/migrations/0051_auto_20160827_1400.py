# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0050_auto_20160827_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='item008',
            name='row01g01',
            field=models.NullBooleanField(verbose_name='外部主件 格林柱 備註說明 => 磨損'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row02g01',
            field=models.NullBooleanField(verbose_name=' 機架底座 備註說明 => 磨損'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row02g02',
            field=models.NullBooleanField(verbose_name=' 機架底座 備註說明 => 裂縫'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row03g01',
            field=models.NullBooleanField(verbose_name=' 模板(定) 備註說明 => 平面變型'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row04g01',
            field=models.NullBooleanField(verbose_name=' 模板(動) 備註說明 => 平面變型'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row05g01',
            field=models.NullBooleanField(verbose_name=' 合模 備註說明 => 合模缸漏油'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row05g02',
            field=models.NullBooleanField(verbose_name=' 合模 備註說明 => 合模缸螺旋斷裂'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row05g03',
            field=models.NullBooleanField(verbose_name=' 合模 備註說明 => 合模活塞磨損'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row06g01',
            field=models.NullBooleanField(verbose_name=' 曲軸 備註說明 => 磨損'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row07g01',
            field=models.NullBooleanField(verbose_name=' 鋼帶 備註說明 => 磨損'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row07g02',
            field=models.NullBooleanField(verbose_name=' 鋼帶 備註說明 => 斷裂'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row08g01',
            field=models.NullBooleanField(verbose_name=' 保温炉 備註說明 => 磨損'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row08g02',
            field=models.NullBooleanField(verbose_name=' 保温炉 備註說明 => 斷裂'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row08g03',
            field=models.NullBooleanField(verbose_name=' 保温炉 備註說明 => 無法修復'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row08g04',
            field=models.NullBooleanField(verbose_name=' 保温炉 備註說明 => 炉盖损坏'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row08g05',
            field=models.NullBooleanField(verbose_name=' 保温炉 備註說明 => 加热管断'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row08g06',
            field=models.NullBooleanField(verbose_name=' 保温炉 備註說明 => 电路断'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row09g01',
            field=models.NullBooleanField(verbose_name='控制系统 膜厚調節 備註說明 => 開關損壞'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row09g02',
            field=models.NullBooleanField(verbose_name='控制系统 膜厚調節 備註說明 => 線路不通'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row09g03',
            field=models.NullBooleanField(verbose_name='控制系统 膜厚調節 備註說明 => 短路'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row10g01',
            field=models.NullBooleanField(verbose_name=' 主电箱 備註說明 => 保险丝烧坏'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row10g02',
            field=models.NullBooleanField(verbose_name=' 主电箱 備註說明 => 線路不通'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row11g01',
            field=models.NullBooleanField(verbose_name=' 操作面板 備註說明 => 按键损坏'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row11g02',
            field=models.NullBooleanField(verbose_name=' 操作面板 備註說明 => 系统坏'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row12g01',
            field=models.NullBooleanField(verbose_name='压射系统  備註說明 => 無壓力'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row12g02',
            field=models.NullBooleanField(verbose_name='压射系统  備註說明 => 線路不通'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row12g03',
            field=models.NullBooleanField(verbose_name='压射系统  備註說明 => 壓射缸漏油'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row12g04',
            field=models.NullBooleanField(verbose_name='压射系统  備註說明 => 射杆彎曲'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row12g05',
            field=models.NullBooleanField(verbose_name='压射系统  備註說明 => 连接板断裂'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row12g06',
            field=models.NullBooleanField(verbose_name='压射系统  備註說明 => 开关无信号'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row12g07',
            field=models.NullBooleanField(verbose_name='压射系统  備註說明 => 料管磨损'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row13g01',
            field=models.NullBooleanField(verbose_name='澆注系統  備註說明 => 链条断'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row13g02',
            field=models.NullBooleanField(verbose_name='澆注系統  備註說明 => 齿轮滑牙斷'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row13g03',
            field=models.NullBooleanField(verbose_name='澆注系統  備註說明 => 編碼器異常'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row14g01',
            field=models.NullBooleanField(verbose_name='油壓系統  備註說明 => 破損'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row14g02',
            field=models.NullBooleanField(verbose_name='油壓系統  備註說明 => 斷裂'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row14g03',
            field=models.NullBooleanField(verbose_name='油壓系統  備註說明 => 接頭滑絲'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row14g04',
            field=models.NullBooleanField(verbose_name='油壓系統  備註說明 => 堵塞'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row14g05',
            field=models.NullBooleanField(verbose_name='油壓系統  備註說明 => 油品變質'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row14g06',
            field=models.NullBooleanField(verbose_name='油壓系統  備註說明 => 磨損'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row14g07',
            field=models.NullBooleanField(verbose_name='油壓系統  備註說明 => 軸心斷裂'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row14g08',
            field=models.NullBooleanField(verbose_name='油壓系統  備註說明 => 線路不通'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row15g01',
            field=models.NullBooleanField(verbose_name='潤滑系統  備註說明 => 管道不通'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row15g02',
            field=models.NullBooleanField(verbose_name='潤滑系統  備註說明 => 管道斷裂'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row16g01',
            field=models.NullBooleanField(verbose_name='氮氣  備註說明 => 鋼瓶裂縫'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row16g02',
            field=models.NullBooleanField(verbose_name='氮氣  備註說明 => 壓力過高'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row16g03',
            field=models.NullBooleanField(verbose_name='氮氣  備註說明 => 壓力過低'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row18g01',
            field=models.NullBooleanField(verbose_name='自動噴霧  備註說明 => 霧化器損壞'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row18g02',
            field=models.NullBooleanField(verbose_name='自動噴霧  備註說明 => 線路不通'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row18g03',
            field=models.NullBooleanField(verbose_name='自動噴霧  備註說明 => 緩衝彈簧斷裂'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row18g04',
            field=models.NullBooleanField(verbose_name='自動噴霧  備註說明 => 喷头螺丝滑牙'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row18g05',
            field=models.NullBooleanField(verbose_name='自動噴霧  備註說明 => 断裂'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row19g01',
            field=models.NullBooleanField(verbose_name='自動取出  備註說明 => 手臂断裂'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row19g02',
            field=models.NullBooleanField(verbose_name='自動取出  備註說明 => 夹手磨损'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row19g03',
            field=models.NullBooleanField(verbose_name='自動取出  備註說明 => 缓冲器坏'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row19g04',
            field=models.NullBooleanField(verbose_name='自動取出  備註說明 => 手臂轴承坏'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row20g01',
            field=models.NullBooleanField(verbose_name='模具  備註說明 => 尺寸NG'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row20g02',
            field=models.NullBooleanField(verbose_name='模具  備註說明 => 模崩'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row20g03',
            field=models.NullBooleanField(verbose_name='模具  備註說明 => 模芯斷'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row20g04',
            field=models.NullBooleanField(verbose_name='模具  備註說明 => 顶针斷'),
        ),
        migrations.AddField(
            model_name='item008',
            name='row20g05',
            field=models.NullBooleanField(verbose_name='模具  備註說明 => 重覆修模'),
        ),
    ]
