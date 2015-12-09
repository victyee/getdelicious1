# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20150430_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sale_price',
        ),
        migrations.AddField(
            model_name='product',
            name='account_number',
            field=models.IntegerField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='bsb',
            field=models.IntegerField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='about_us',
            field=models.TextField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='operating_state',
            field=models.CharField(default=1, max_length=120, choices=[(b'ACT', b'Australian Capital Territory'), (b'NSW', b'New South Wales'), (b'NT', b'Northern Territory'), (b'QLD', b'Queensland'), (b'SA', b'South Australia'), (b'TAS', b'Tasmania'), (b'VIC', b'Victoria'), (b'WA', b'Western Australia')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='slogan',
            field=models.TextField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
