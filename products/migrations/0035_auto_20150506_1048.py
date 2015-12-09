# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_auto_20150506_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='minimum_guests',
            field=models.DecimalField(max_digits=1000, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variation',
            name='price_per_guest',
            field=models.DecimalField(max_digits=1000, decimal_places=2),
            preserve_default=True,
        ),
    ]
