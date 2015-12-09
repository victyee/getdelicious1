# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20150501_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='maximum_guests',
            field=models.DecimalField(default=1, max_digits=1000, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variation',
            name='mininum_guests',
            field=models.DecimalField(default=1, max_digits=1000, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variation',
            name='price_per_guest',
            field=models.DecimalField(default=1, max_digits=1000, decimal_places=2),
            preserve_default=False,
        ),
    ]
