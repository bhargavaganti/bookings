# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('concept', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=250)),
                ('caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.Caja')),
            ],
        ),
    ]
