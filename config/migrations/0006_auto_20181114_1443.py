# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-14 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_auto_20181030_0937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agencyallotmentdetail',
            options={'verbose_name': 'Agency Accomodation Detail', 'verbose_name_plural': 'Agency Accomodation Details'},
        ),
        migrations.AlterModelOptions(
            name='agencyallotmentservice',
            options={'verbose_name': 'Agency Accomodation Service', 'verbose_name_plural': 'Agency Accomodation Services'},
        ),
        migrations.AlterModelOptions(
            name='allotment',
            options={'verbose_name': 'Accomodation', 'verbose_name_plural': 'Accomodation'},
        ),
        migrations.AlterModelOptions(
            name='allotmentboardtype',
            options={'verbose_name': 'Accomodation Board Type', 'verbose_name_plural': 'Accomodation Board Types'},
        ),
        migrations.AlterModelOptions(
            name='allotmentroomavailability',
            options={'verbose_name': 'Accomodation Availability', 'verbose_name_plural': 'Accomodation Availabilities'},
        ),
        migrations.AlterModelOptions(
            name='allotmentsupplement',
            options={'verbose_name': 'Accomodation Supplement', 'verbose_name_plural': 'Accomodation Supplements'},
        ),
        migrations.AlterModelOptions(
            name='providerallotmentdetail',
            options={'verbose_name': 'Accomodation Provider Detail', 'verbose_name_plural': 'Accomodation Provider Details'},
        ),
        migrations.AlterModelOptions(
            name='providerallotmentservice',
            options={'verbose_name': 'Accomodation Service Provider', 'verbose_name_plural': 'Accomodation Service Providers'},
        ),
    ]