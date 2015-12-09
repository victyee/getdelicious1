# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_remove_variation_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='extra_hours_charge',
            field=models.DecimalField(default=0, max_digits=1000, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variation',
            name='extra_km_charge',
            field=models.DecimalField(default=0, max_digits=1000, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variation',
            name='included_service_hours',
            field=models.DecimalField(default=0, max_digits=1000, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variation',
            name='included_travel_distance',
            field=models.DecimalField(default=0, max_digits=1000, decimal_places=2),
            preserve_default=True,
        ),
    ]
