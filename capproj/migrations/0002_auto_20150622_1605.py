# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capproj', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='bond_series',
            new_name='bond_series_number',
        ),
    ]
