# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-07 01:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_finantialdocument_details'),
        ('config', '0005_auto_20181030_0937'),
        ('booking', '0010_auto_20181106_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('reference', models.CharField(max_length=250)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('date_to', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('DR', 'Draft'), ('RD', 'Ready')], default='DR', max_length=5)),
                ('currency', models.CharField(choices=[('CUC', 'CUC'), ('USD', 'USD'), ('EUR', 'EUR')], default='CUC', max_length=5)),
                ('currency_factor', models.DecimalField(decimal_places=6, default=1.0, max_digits=12)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Agency')),
            ],
            options={
                'verbose_name': 'Quote',
                'verbose_name_plural': 'Quotes',
            },
        ),
        migrations.CreateModel(
            name='QuotePaxVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pax_quantity', models.SmallIntegerField()),
                ('cost_single_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cost Single')),
                ('cost_double_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cost Double')),
                ('cost_triple_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cost Triple')),
                ('price_single_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price Single')),
                ('price_double_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price Double')),
                ('price_triple_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price Triple')),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote_paxvariants', to='booking.Quote')),
            ],
            options={
                'verbose_name': 'Quote Pax',
                'verbose_name_plural': 'Quotes Paxes',
            },
        ),
        migrations.CreateModel(
            name='QuoteService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Quote Service', max_length=250)),
                ('service_type', models.CharField(blank=True, choices=[('E', 'Extra'), ('A', 'Allotment'), ('T', 'Transfer')], max_length=5, null=True)),
                ('description', models.CharField(default='', max_length=1000)),
                ('datetime_from', models.DateTimeField(blank=True, null=True)),
                ('datetime_to', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PD', 'Pending'), ('RQ', 'Requested'), ('PH', 'Phone Confirmed'), ('OK', 'Confirmed'), ('CD', 'Coordinated'), ('CN', 'Cancelled')], default='PD', max_length=5)),
            ],
            options={
                'verbose_name': 'Quote Service',
                'verbose_name_plural': 'Quote Services',
            },
        ),
        migrations.CreateModel(
            name='QuoteAllotment',
            fields=[
                ('quoteservice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking.QuoteService')),
                ('board_type', models.CharField(choices=[('NB', 'None Board'), ('BB', 'Breakfast Board'), ('HB', 'Half Board'), ('FB', 'Full Board'), ('AI', 'All Included')], max_length=5)),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.RoomType')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.Allotment')),
            ],
            options={
                'verbose_name': 'Quote Allotment',
                'verbose_name_plural': 'Quotes Allotments',
            },
            bases=('booking.quoteservice',),
        ),
        migrations.CreateModel(
            name='QuoteExtra',
            fields=[
                ('quoteservice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking.QuoteService')),
                ('parameter', models.SmallIntegerField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.Extra')),
            ],
            options={
                'verbose_name': 'Quote Extra',
                'verbose_name_plural': 'Quotes Extras',
            },
            bases=('booking.quoteservice',),
        ),
        migrations.CreateModel(
            name='QuoteTransfer',
            fields=[
                ('quoteservice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking.QuoteService')),
                ('location_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote_location_from', to='config.Location', verbose_name='Location from')),
                ('location_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote_location_to', to='config.Location', verbose_name='Location to')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.Transfer')),
            ],
            options={
                'verbose_name': 'Quote Transfer',
                'verbose_name_plural': 'Quotes Transfers',
            },
            bases=('booking.quoteservice',),
        ),
        migrations.AddField(
            model_name='quoteservice',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.Provider'),
        ),
        migrations.AddField(
            model_name='quoteservice',
            name='quote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote_services', to='booking.Quote'),
        ),
        migrations.AlterUniqueTogether(
            name='quotepaxvariant',
            unique_together=set([('quote', 'pax_quantity')]),
        ),
    ]
