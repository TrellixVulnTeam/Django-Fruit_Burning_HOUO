# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-15 20:43
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_nun', models.CharField(max_length=30, verbose_name='订单号')),
                ('order_transationnun', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='交易号')),
                ('order_status', models.CharField(choices=[('TRADE_SUCCESS', '成功'), ('TRADE_CLOSED', '超时关闭'), ('WAIT_BUYER_PAY', '交易创建'), ('TRADE_FINISHED', '交易结束'), ('paying', '待支付')], default='paying', max_length=30, verbose_name='订单状态')),
                ('order_mount', models.FloatField(default=0.0, verbose_name='订单金额')),
                ('order_paytime', models.DateTimeField(blank=True, null=True, verbose_name='支付时间')),
                ('order_extra', models.TextField(verbose_name='备注')),
                ('order_logistics', models.CharField(max_length=30, verbose_name='物流信息')),
                ('order_updatetime', models.DateTimeField(auto_now=True, verbose_name='订单更新时间')),
                ('order_addtime', models.DateTimeField(auto_now_add=True, verbose_name='下单时间')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.shop', verbose_name='店铺')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
                'db_table': 'fb_order',
            },
        ),
        migrations.CreateModel(
            name='order_goods',
            fields=[
                ('order_goods_id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_num', models.IntegerField(default=0, verbose_name='商品数量')),
                ('order_goods_addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='商品')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='trade.order', verbose_name='订单信息')),
            ],
            options={
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
                'db_table': 'fb_order_goods',
            },
        ),
        migrations.CreateModel(
            name='shoppingcart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoppingcart_nums', models.IntegerField(default=0, verbose_name='购买数量')),
                ('shoppingcart_addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='商品加入时间')),
                ('goods', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='商品')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'db_table': 'fb_shoppingcart',
            },
        ),
        migrations.AlterUniqueTogether(
            name='shoppingcart',
            unique_together=set([('user', 'goods')]),
        ),
    ]
