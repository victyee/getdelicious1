# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20150501_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='contact_number',
            field=models.IntegerField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='foodtruck_name',
            field=models.CharField(max_length=120),
            preserve_default=True,
        ),
    ]
