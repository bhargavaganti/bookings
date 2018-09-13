# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-10 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20180906_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookingservice',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='booking.Booking'),
        ),
    ]
