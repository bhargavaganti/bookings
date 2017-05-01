# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 18:56
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cuentas', '0004_auto_20170415_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='reference_type',
            field=models.CharField(choices=[('BANK_TRANSFER', 'Bank Transfer'), ('CASH', 'Cash'), ('NONE', 'None')], default='NONE', max_length=30),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(default=1, help_text='User who performed the action.', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='caja',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 5, 1, 14, 54, 54, 579279)),
        ),
        migrations.AlterField(
            model_name='caja',
            name='modified',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 5, 1, 14, 54, 54, 579308)),
        ),
    ]
