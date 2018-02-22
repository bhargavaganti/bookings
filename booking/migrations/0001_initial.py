# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('config', '0001_initial'),
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('deleted', models.BooleanField(default=False)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.Agency')),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Operation')),
            ],
        ),
        migrations.CreateModel(
            name='AgencyPaymentInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('agency_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.AgencyPayment')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('list_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=1000)),
                ('reference', models.CharField(max_length=256)),
                ('deleted', models.BooleanField(default=False)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.Agency')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.Office')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookingAccomodationPax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtty', models.SmallIntegerField(default=1)),
                ('pax', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.PaxType')),
            ],
        ),
        migrations.CreateModel(
            name='BookingService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('list_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=1000)),
                ('qtty', models.SmallIntegerField(default=1)),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('file', models.FileField(upload_to='')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='ProviderPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('deleted', models.BooleanField(default=False)),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Operation')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.Provider')),
            ],
        ),
        migrations.CreateModel(
            name='ProviderPaymentBookingService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='BookingAccomodation',
            fields=[
                ('bookingservice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking.BookingService')),
                ('pax_description', models.CharField(max_length=40)),
                ('board_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.BoardType')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.RoomType')),
            ],
            options={
                'abstract': False,
            },
            bases=('booking.bookingservice',),
        ),
        migrations.AddField(
            model_name='providerpaymentbookingservice',
            name='booking_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.BookingService'),
        ),
        migrations.AddField(
            model_name='providerpaymentbookingservice',
            name='operation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Operation'),
        ),
        migrations.AddField(
            model_name='providerpaymentbookingservice',
            name='provider_payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.ProviderPayment'),
        ),
        migrations.AddField(
            model_name='bookingservice',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Booking'),
        ),
        migrations.AddField(
            model_name='bookingservice',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.Provider'),
        ),
        migrations.AddField(
            model_name='bookingservice',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.Service'),
        ),
        migrations.AddField(
            model_name='agencypaymentinvoice',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Invoice'),
        ),
        migrations.AddField(
            model_name='agencypaymentinvoice',
            name='operation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Operation'),
        ),
        migrations.AddField(
            model_name='bookingaccomodationpax',
            name='booking_accomodation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.BookingAccomodation'),
        ),
    ]
