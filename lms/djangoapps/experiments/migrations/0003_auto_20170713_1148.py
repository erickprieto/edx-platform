# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0002_auto_20170627_1402'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experimentkeyvalue',
            options={'verbose_name': 'Experiment Key-Value Pair', 'verbose_name_plural': 'Experiment Key-Value Pairs'},
        ),
    ]
