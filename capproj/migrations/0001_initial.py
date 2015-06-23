# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('idno', models.CharField(null=True, blank=True, max_length=10)),
                ('admin_agency', models.CharField(null=True, blank=True, max_length=500)),
                ('email', models.CharField(null=True, blank=True, max_length=500)),
                ('url', models.CharField(null=True, blank=True, max_length=500)),
                ('year', models.CharField(max_length=4)),
                ('approp_title', models.CharField(max_length=500)),
                ('fund_code', models.CharField(null=True, blank=True, max_length=500)),
                ('eligibility', models.CharField(null=True, blank=True, max_length=500)),
                ('bond_sale_date', models.CharField(null=True, blank=True, max_length=500)),
                ('bond_series', models.CharField(null=True, blank=True, max_length=500)),
                ('amount_of_bond', models.IntegerField(null=True, blank=True)),
                ('category', models.CharField(null=True, blank=True, max_length=500)),
                ('subcategory', models.CharField(null=True, blank=True, max_length=500)),
                ('county', models.CharField(null=True, blank=True, max_length=500)),
                ('state_amount', models.IntegerField(null=True, blank=True)),
                ('amount_reauthorized', models.IntegerField(null=True, blank=True)),
                ('reversion_date', models.CharField(null=True, blank=True, max_length=500)),
                ('valid_encumbrance', models.IntegerField(null=True, blank=True)),
                ('expended_amount', models.IntegerField(null=True, blank=True)),
                ('aipp_amount_bof', models.IntegerField(null=True, blank=True)),
                ('reversion_amount', models.IntegerField(null=True, blank=True)),
                ('appropriation_balance', models.IntegerField(null=True, blank=True)),
                ('last_update', models.CharField(null=True, blank=True, max_length=500)),
                ('icip_project_number', models.CharField(null=True, blank=True, max_length=500)),
                ('icip_priority_number', models.CharField(null=True, blank=True, max_length=500)),
                ('local_fiscal_agent', models.CharField(null=True, blank=True, max_length=500)),
                ('amount_obligated', models.IntegerField(null=True, blank=True)),
                ('project_end_date', models.CharField(null=True, blank=True, max_length=500)),
                ('expended_amount_state', models.IntegerField(null=True, blank=True)),
                ('aipp_amount', models.IntegerField(null=True, blank=True)),
                ('reauth_of_balance_to_new', models.IntegerField(null=True, blank=True)),
                ('reauth_to_project_number', models.CharField(null=True, blank=True, max_length=500)),
                ('reversion_amount_two', models.IntegerField(null=True, blank=True)),
                ('project_status', models.TextField(null=True, blank=True)),
                ('goal_milestone_last_quarter', models.TextField(null=True, blank=True)),
                ('goal_milestone_next_quarter', models.TextField(null=True, blank=True)),
                ('project_phase', models.CharField(null=True, blank=True, max_length=500)),
                ('current_balance', models.IntegerField(null=True, blank=True)),
                ('last_agency_update', models.CharField(null=True, blank=True, max_length=500)),
                ('last_submission_date', models.CharField(null=True, blank=True, max_length=500)),
                ('expended_amount_local', models.IntegerField(null=True, blank=True)),
                ('current_balance_local', models.IntegerField(null=True, blank=True)),
                ('project_status_local', models.TextField(null=True, blank=True)),
                ('goal_milestone_last_quarter_local', models.TextField(null=True, blank=True)),
                ('goal_milestone_next_quarter_local', models.TextField(null=True, blank=True)),
                ('valid_contracts_in_place', models.NullBooleanField()),
                ('no_activity_for_month', models.NullBooleanField()),
                ('last_submission_date_local', models.CharField(null=True, blank=True, max_length=500)),
                ('last_update_local', models.CharField(null=True, blank=True, max_length=500)),
                ('progress', models.CharField(choices=[('C', 'Completed'), ('S', 'Started'), ('N', 'Not started'), ('P', 'Partially completed'), ('?', 'Unclear')], default='?', max_length=30)),
                ('contractor_vendor', models.CharField(null=True, blank=True, max_length=500)),
                ('contractor_location', models.CharField(null=True, blank=True, max_length=500)),
                ('sponsors', models.CharField(null=True, blank=True, max_length=1000)),
                ('reporter_notes', models.TextField(null=True, blank=True)),
                ('public_description', models.TextField(null=True, blank=True)),
                ('photo', models.ImageField(upload_to='media', null=True, blank=True)),
                ('reporter_name', models.CharField(null=True, blank=True, max_length=500)),
                ('reporter_org', models.CharField(null=True, blank=True, max_length=500)),
            ],
        ),
    ]
