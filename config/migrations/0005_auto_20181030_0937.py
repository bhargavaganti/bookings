# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-30 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_auto_20181029_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='extra',
            name='max_capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transfer',
            name='max_capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='SGL'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='DBL'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='TPL'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='QAD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_1_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_1_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_1_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_1_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_1_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_2_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_2_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_2_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_2_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_2_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_3_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_3_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_3_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_3_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyallotmentdetail',
            name='ch_3_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='SGL'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='DBL'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='TPL'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='QAD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_1_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_1_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_1_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_1_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_1_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_2_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_2_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_2_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_2_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_2_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_3_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_3_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_3_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_3_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencyextradetail',
            name='ch_3_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='a_location_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_location_from', to='config.Location', verbose_name='Location from'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='a_location_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_location_to', to='config.Location', verbose_name='Location to'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='SGL'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='DBL'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='TPL'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='QAD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_1_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_1_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_1_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_1_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_1_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_2_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_2_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_2_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_2_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_2_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_3_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_3_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_3_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_3_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='agencytransferdetail',
            name='ch_3_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='SGL'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='DBL'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='TPL'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='QAD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_1_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_1_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_1_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_1_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_1_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_2_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_2_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_2_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_2_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_2_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_3_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_3_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_3_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_3_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providerallotmentdetail',
            name='ch_3_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='SGL'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='DBL'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='TPL'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='QAD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_1_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_1_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_1_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_1_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_1_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_2_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_2_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_2_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_2_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_2_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_3_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_3_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_3_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_3_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providerextradetail',
            name='ch_3_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='SGL'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='DBL'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='TPL'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='QAD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_1_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_1_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_1_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_1_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_1_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='1st CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_2_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_2_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_2_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_2_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_2_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='2nd CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_3_ad_0_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_3_ad_1_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_3_ad_2_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_3_ad_3_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='ch_3_ad_4_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='3rd CHD'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='p_location_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_location_from', to='config.Location', verbose_name='Location from'),
        ),
        migrations.AlterField(
            model_name='providertransferdetail',
            name='p_location_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_location_to', to='config.Location', verbose_name='Location to'),
        ),
    ]
