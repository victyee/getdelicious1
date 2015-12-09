# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_variation_included_service_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='extra_hours_charge',
            field=models.IntegerField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='variation',
            name='extra_km_charge',
            field=models.IntegerField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='variation',
            name='included_travel_distance',
            field=models.IntegerField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
    ]
