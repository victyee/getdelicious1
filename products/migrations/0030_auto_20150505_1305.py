# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_auto_20150504_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='extra_hours_charge',
            field=models.DecimalField(null=True, max_digits=1000, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variation',
            name='extra_km_charge',
            field=models.DecimalField(null=True, max_digits=1000, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variation',
            name='included_service_hours',
            field=models.DecimalField(max_digits=1000, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variation',
            name='included_travel_distance',
            field=models.DecimalField(null=True, max_digits=1000, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
