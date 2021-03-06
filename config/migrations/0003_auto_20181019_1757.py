# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-19 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_location_short_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agencyallotmentservice',
            name='cost_type',
        ),
        migrations.RemoveField(
            model_name='agencyextraservice',
            name='cost_type',
        ),
        migrations.RemoveField(
            model_name='agencytransferservice',
            name='cost_type',
        ),
        migrations.RemoveField(
            model_name='providerallotmentservice',
            name='cost_type',
        ),
        migrations.RemoveField(
            model_name='providerextraservice',
            name='cost_type',
        ),
        migrations.RemoveField(
            model_name='providertransferservice',
            name='cost_type',
        ),
        migrations.AddField(
            model_name='extra',
            name='cost_type',
            field=models.CharField(choices=[('F', 'Fixed'), ('P', 'By Pax')], default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extra',
            name='parameter_type',
            field=models.CharField(choices=[('H', 'Hours'), ('D', 'Days')], default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfer',
            name='cost_type',
            field=models.CharField(choices=[('F', 'Fixed'), ('P', 'By Pax')], default=1, max_length=5),
            preserve_default=False,
        ),
    ]
