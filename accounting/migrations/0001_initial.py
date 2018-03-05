# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 21:59
from __future__ import unicode_literals

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
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('currency', models.CharField(choices=[('CUC', 'cuc'), ('USD', 'usd'), ('EUR', 'eur')], default='CUC', max_length=5)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('allow_negative', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField(default=0)),
                ('concept', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=500)),
                ('credit_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_account', to='accounting.Account')),
                ('debit_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debit_account', to='accounting.Account')),
                ('user', models.ForeignKey(help_text='User who performed the action.', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Movement',
                'verbose_name_plural': 'Movements',
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('operation_type', models.CharField(choices=[('CURRENCY_CONVERSION', 'Currency Conversion'), ('TRANSFER', 'Transfer'), ('LOAN', 'Loan'), ('DEVOLUTION', 'Devolution'), ('INCOME', 'Income'), ('CONSUMPTION', 'Consumption'), ('INVOICE_EMITTED', 'Currency Conversion'), ('INVOICE_MODIFIED', 'Transfer'), ('INVOICE_CANCELLED', 'Loan'), ('SERVICE_CONFIRMED', 'Devolution'), ('SERVICE_MODIFIED', 'Income'), ('SERVICE_CANCELLED', 'Consumption')], max_length=50)),
                ('concept', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=500)),
                ('user', models.ForeignKey(help_text='User who performed the action.', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Operation',
                'verbose_name_plural': 'Operations',
            },
        ),
        migrations.CreateModel(
            name='OperationMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Movement')),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Operation')),
            ],
            options={
                'verbose_name': 'Operation Movement',
                'verbose_name_plural': 'Operations Movements',
            },
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([('name', 'currency')]),
        ),
    ]