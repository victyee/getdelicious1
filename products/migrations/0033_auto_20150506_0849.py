# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20150505_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='minimum_guests',
            field=models.TextField(max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='variation',
            name='price_per_guest',
            field=models.TextField(max_length=1000),
            preserve_default=True,
        ),
    ]
