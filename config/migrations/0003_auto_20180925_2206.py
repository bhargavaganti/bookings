# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-26 02:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
        ('config', '0002_auto_20180925_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyAllotmentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('board_type', models.CharField(choices=[('NB', 'None Board'), ('BB', 'Breakfast Board'), ('HB', 'Half Board'), ('FB', 'Full Board'), ('AI', 'All Included')], max_length=5)),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.RoomType')),
            ],
            options={
                'verbose_name': 'Agency Allotment Detail',
                'verbose_name_plural': 'Agencies Allotments Details',
            },
        ),
        migrations.CreateModel(
            name='AgencyExtraDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
            options={
                'verbose_name': 'Agency Extra Detail',
                'verbose_name_plural': 'Agencies Extras Details',
            },
        ),
        migrations.CreateModel(
            name='AgencyServiceCatalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
            ],
            options={
                'verbose_name': 'Agency Service Catalogue',
                'verbose_name_plural': 'Agencies Services Catalogues',
            },
        ),
        migrations.CreateModel(
            name='AgencyTransferDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('a_location_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_location_from', to='config.Location')),
                ('a_location_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_location_to', to='config.Location')),
            ],
            options={
                'verbose_name': 'Agency Transfer Detail',
                'verbose_name_plural': 'Agencies Transfers Details',
            },
        ),
        migrations.CreateModel(
            name='ProviderAllotmentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('board_type', models.CharField(choices=[('NB', 'None Board'), ('BB', 'Breakfast Board'), ('HB', 'Half Board'), ('FB', 'Full Board'), ('AI', 'All Included')], max_length=5)),
            ],
            options={
                'verbose_name': 'Provider Allotment Detail',
                'verbose_name_plural': 'Providers Allotments Details',
            },
        ),
        migrations.CreateModel(
            name='ProviderExtraDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
            options={
                'verbose_name': 'Provider Extra Detail',
                'verbose_name_plural': 'Providers Extras Details',
            },
        ),
        migrations.CreateModel(
            name='ProviderServiceCatalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Provider')),
            ],
            options={
                'verbose_name': 'Provider Service Catalogue',
                'verbose_name_plural': 'Providers Services Catalogues',
            },
        ),
        migrations.CreateModel(
            name='ProviderTransferDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_1_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_2_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_0_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_3_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('ch_3_ad_4_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('p_location_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_location_from', to='config.Location')),
                ('p_location_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_location_to', to='config.Location')),
            ],
            options={
                'verbose_name': 'Provider Transfer Detail',
                'verbose_name_plural': 'Providers Transfers Details',
            },
        ),
        migrations.RenameModel(
            old_name='AllotmentServiceProvider',
            new_name='ProviderAllotmentService',
        ),
        migrations.RenameModel(
            old_name='ExtraServiceProvider',
            new_name='ProviderExtraService',
        ),
        migrations.RenameModel(
            old_name='TransferServiceProvider',
            new_name='ProviderTransferService',
        ),
        migrations.RemoveField(
            model_name='allotmentcost',
            name='service_provider',
        ),
        migrations.AlterUniqueTogether(
            name='allotmentcostdetail',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='allotmentcostdetail',
            name='board_type',
        ),
        migrations.RemoveField(
            model_name='allotmentcostdetail',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='allotmentcostdetail',
            name='room_type',
        ),
        migrations.AlterUniqueTogether(
            name='allotmentcostdetailprice',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='allotmentcostdetailprice',
            name='catalogue',
        ),
        migrations.RemoveField(
            model_name='allotmentcostdetailprice',
            name='cost_detail',
        ),
        migrations.AlterUniqueTogether(
            name='allotmentsupplementcostdetail',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='allotmentsupplementcostdetail',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='allotmentsupplementcostdetail',
            name='supplement',
        ),
        migrations.RemoveField(
            model_name='allotmentsupplementcostdetailprice',
            name='catalogue',
        ),
        migrations.RemoveField(
            model_name='allotmentsupplementcostdetailprice',
            name='supplement_cost_detail',
        ),
        migrations.RemoveField(
            model_name='extracost',
            name='service_provider',
        ),
        migrations.AlterUniqueTogether(
            name='extracostdetail',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='extracostdetail',
            name='cost',
        ),
        migrations.AlterUniqueTogether(
            name='extracostdetailprice',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='extracostdetailprice',
            name='catalogue',
        ),
        migrations.RemoveField(
            model_name='extracostdetailprice',
            name='cost_detail',
        ),
        migrations.AlterUniqueTogether(
            name='extrasupplementcostdetail',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='extrasupplementcostdetail',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='extrasupplementcostdetail',
            name='supplement',
        ),
        migrations.RemoveField(
            model_name='extrasupplementcostdetailprice',
            name='catalogue',
        ),
        migrations.RemoveField(
            model_name='extrasupplementcostdetailprice',
            name='supplement_cost_detail',
        ),
        migrations.DeleteModel(
            name='PriceCatalogue',
        ),
        migrations.AlterUniqueTogether(
            name='serviceprovider',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='service',
        ),
        migrations.AlterUniqueTogether(
            name='serviceproviderprice',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='serviceproviderprice',
            name='catalogue',
        ),
        migrations.RemoveField(
            model_name='serviceproviderprice',
            name='service_provider',
        ),
        migrations.RemoveField(
            model_name='transfercost',
            name='service_provider',
        ),
        migrations.AlterUniqueTogether(
            name='transfercostdetail',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='transfercostdetail',
            name='cost',
        ),
        migrations.AlterUniqueTogether(
            name='transfercostdetailprice',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='transfercostdetailprice',
            name='catalogue',
        ),
        migrations.RemoveField(
            model_name='transfercostdetailprice',
            name='cost_detail',
        ),
        migrations.AlterUniqueTogether(
            name='transfersupplementcostdetail',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='transfersupplementcostdetail',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='transfersupplementcostdetail',
            name='supplement',
        ),
        migrations.RemoveField(
            model_name='transfersupplementcostdetailprice',
            name='catalogue',
        ),
        migrations.RemoveField(
            model_name='transfersupplementcostdetailprice',
            name='supplement_cost_detail',
        ),
        migrations.AlterModelOptions(
            name='providerallotmentservice',
            options={'verbose_name': 'Provider Allotment Service', 'verbose_name_plural': 'Providers Allotments Services'},
        ),
        migrations.AlterModelOptions(
            name='providerextraservice',
            options={'verbose_name': 'Provider Extra Service', 'verbose_name_plural': 'Providers Extras Services'},
        ),
        migrations.AlterModelOptions(
            name='providertransferservice',
            options={'verbose_name': 'Provider Transfer Service', 'verbose_name_plural': 'Providers Transfers Services'},
        ),
        migrations.RemoveField(
            model_name='providerallotmentservice',
            name='serviceprovider_ptr',
        ),
        migrations.RemoveField(
            model_name='providerextraservice',
            name='serviceprovider_ptr',
        ),
        migrations.RemoveField(
            model_name='providertransferservice',
            name='serviceprovider_ptr',
        ),
        migrations.AlterUniqueTogether(
            name='agencypricecatalogue',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='agencypricecatalogue',
            name='agency',
        ),
        migrations.RemoveField(
            model_name='agencypricecatalogue',
            name='price_catalogue',
        ),
        migrations.AddField(
            model_name='service',
            name='child_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='AgencyAllotmentService',
            fields=[
                ('agencyservicecatalogue_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='config.AgencyServiceCatalogue')),
                ('cost_type', models.CharField(choices=[('F', 'Fixed'), ('P', 'By Pax')], max_length=5)),
            ],
            options={
                'verbose_name': 'Agency Allotment Service',
                'verbose_name_plural': 'Agencies Allotments Services',
            },
            bases=('config.agencyservicecatalogue',),
        ),
        migrations.CreateModel(
            name='AgencyExtraService',
            fields=[
                ('agencyservicecatalogue_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='config.AgencyServiceCatalogue')),
                ('cost_type', models.CharField(choices=[('P', 'By Pax'), ('E', 'By Extra'), ('PE', 'By Pax Extra')], max_length=5)),
            ],
            options={
                'verbose_name': 'Provider Extra Service',
                'verbose_name_plural': 'Providers Extras Services',
            },
            bases=('config.agencyservicecatalogue',),
        ),
        migrations.CreateModel(
            name='AgencyTransferService',
            fields=[
                ('agencyservicecatalogue_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='config.AgencyServiceCatalogue')),
                ('cost_type', models.CharField(choices=[('F', 'Fixed'), ('P', 'By Pax')], max_length=5)),
            ],
            options={
                'verbose_name': 'Agency Transfer Service',
                'verbose_name_plural': 'Agencies Transfers Services',
            },
            bases=('config.agencyservicecatalogue',),
        ),
        migrations.DeleteModel(
            name='AgencyPriceCatalogue',
        ),
        migrations.DeleteModel(
            name='AllotmentCost',
        ),
        migrations.DeleteModel(
            name='AllotmentCostDetail',
        ),
        migrations.DeleteModel(
            name='AllotmentCostDetailPrice',
        ),
        migrations.DeleteModel(
            name='AllotmentSupplementCostDetail',
        ),
        migrations.DeleteModel(
            name='AllotmentSupplementCostDetailPrice',
        ),
        migrations.DeleteModel(
            name='ExtraCost',
        ),
        migrations.DeleteModel(
            name='ExtraCostDetail',
        ),
        migrations.DeleteModel(
            name='ExtraCostDetailPrice',
        ),
        migrations.DeleteModel(
            name='ExtraSupplementCostDetail',
        ),
        migrations.DeleteModel(
            name='ExtraSupplementCostDetailPrice',
        ),
        migrations.DeleteModel(
            name='ServiceProvider',
        ),
        migrations.DeleteModel(
            name='ServiceProviderPrice',
        ),
        migrations.DeleteModel(
            name='TransferCost',
        ),
        migrations.DeleteModel(
            name='TransferCostDetail',
        ),
        migrations.DeleteModel(
            name='TransferCostDetailPrice',
        ),
        migrations.DeleteModel(
            name='TransferSupplementCostDetail',
        ),
        migrations.DeleteModel(
            name='TransferSupplementCostDetailPrice',
        ),
        migrations.AddField(
            model_name='providertransferdetail',
            name='provider_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.ProviderTransferService'),
        ),
        migrations.AddField(
            model_name='providerservicecatalogue',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.Service'),
        ),
        migrations.AddField(
            model_name='providerextradetail',
            name='provider_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.ProviderExtraService'),
        ),
        migrations.AddField(
            model_name='providerallotmentdetail',
            name='provider_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.ProviderAllotmentService'),
        ),
        migrations.AddField(
            model_name='providerallotmentdetail',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.RoomType'),
        ),
        migrations.AddField(
            model_name='agencyservicecatalogue',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Agency'),
        ),
        migrations.AddField(
            model_name='agencyservicecatalogue',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.Service'),
        ),
        migrations.AddField(
            model_name='providerallotmentservice',
            name='providerservicecatalogue_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='config.ProviderServiceCatalogue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='providerextraservice',
            name='providerservicecatalogue_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='config.ProviderServiceCatalogue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='providertransferservice',
            name='providerservicecatalogue_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='config.ProviderServiceCatalogue'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='providertransferdetail',
            unique_together=set([('provider_service', 'p_location_from', 'p_location_to')]),
        ),
        migrations.AlterUniqueTogether(
            name='providerextradetail',
            unique_together=set([('provider_service',)]),
        ),
        migrations.AlterUniqueTogether(
            name='providerallotmentdetail',
            unique_together=set([('provider_service', 'room_type', 'board_type')]),
        ),
        migrations.AddField(
            model_name='agencytransferdetail',
            name='agency_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.AgencyTransferService'),
        ),
        migrations.AddField(
            model_name='agencyextradetail',
            name='agency_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.AgencyExtraService'),
        ),
        migrations.AddField(
            model_name='agencyallotmentdetail',
            name='agency_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.AgencyAllotmentService'),
        ),
        migrations.AlterUniqueTogether(
            name='agencytransferdetail',
            unique_together=set([('agency_service', 'a_location_from', 'a_location_to')]),
        ),
        migrations.AlterUniqueTogether(
            name='agencyextradetail',
            unique_together=set([('agency_service',)]),
        ),
        migrations.AlterUniqueTogether(
            name='agencyallotmentdetail',
            unique_together=set([('agency_service', 'room_type', 'board_type')]),
        ),
    ]
