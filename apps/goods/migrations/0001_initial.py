# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-15 20:43
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='goods',
            fields=[
                ('goods_id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=30, verbose_name='商品名')),
                ('goods_price', models.FloatField(default=0, verbose_name='商品价格')),
                ('goods_pickTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='采摘日期')),
                ('goods_shelflife', models.IntegerField(verbose_name='商品保质期')),
                ('goods_desc', DjangoUeditor.models.UEditorField(default='', verbose_name='商品详情')),
                ('goods_front_image', models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='外面封面图')),
                ('goods_weight', models.CharField(max_length=10, verbose_name='商品重量')),
                ('goods_updateTime', models.DateTimeField(auto_now=True, verbose_name='商品上次更新时间')),
                ('goods_extra', models.TextField(verbose_name='商品备注')),
                ('goods_title', models.CharField(max_length=100, verbose_name='商品标题')),
                ('goods_productarea', models.CharField(max_length=20, verbose_name='产地')),
                ('goods_dateadded', models.DateTimeField(auto_now_add=True, verbose_name='上架日期')),
                ('goods_post', models.BooleanField(verbose_name='是否承担运费')),
                ('goods_stock', models.IntegerField(default=0, verbose_name='总库存')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'fb_goods',
            },
        ),
        migrations.CreateModel(
            name='goodsimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='goods.goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
                'db_table': 'fb_goodsimage',
            },
        ),
        migrations.CreateModel(
            name='shop',
            fields=[
                ('shop_id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_name', models.CharField(max_length=20, verbose_name='店铺名')),
                ('shop_address', models.CharField(max_length=50, verbose_name='店铺地址')),
                ('shop_phone', models.CharField(max_length=11, verbose_name='联系方式')),
                ('shop_extra', models.TextField(verbose_name='店铺信息')),
                ('shop_updateTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('shop_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '店铺',
                'verbose_name_plural': '店铺',
                'db_table': 'fb_shop',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.shop', verbose_name='所属店铺'),
        ),
    ]