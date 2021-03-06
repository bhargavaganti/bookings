# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-31 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_auto_20181030_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='description',
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default='Ronny Larsen x2', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='reference',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[(b'PD', b'Pending'), (b'RQ', b'Requested'), (b'OK', b'Confirmed')], default=b'PD', max_length=5),
        ),
        migrations.AlterField(
            model_name='orderpaxvariant',
            name='cost_double_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name=b'Cost Double'),
        ),
        migrations.AlterField(
            model_name='orderpaxvariant',
            name='cost_single_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name=b'Cost Single'),
        ),
        migrations.AlterField(
            model_name='orderpaxvariant',
            name='cost_triple_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name=b'Cost Triple'),
        ),
        migrations.AlterField(
            model_name='orderpaxvariant',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_paxvariants', to='booking.Order'),
        ),
        migrations.AlterField(
            model_name='orderpaxvariant',
            name='price_double_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name=b'Price Double'),
        ),
        migrations.AlterField(
            model_name='orderpaxvariant',
            name='price_single_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name=b'Price Single'),
        ),
        migrations.AlterField(
            model_name='orderpaxvariant',
            name='price_triple_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name=b'Price Triple'),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='name',
            field=models.CharField(default=b'Order Service', max_length=250),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_services', to='booking.Order'),
        ),
    ]
